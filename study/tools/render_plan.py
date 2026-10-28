"""Render the shareable 42-day plan from ``study/schedule.json``.

This renderer deliberately does not inspect or write ``study/notes``.  The
schedule and generated task cards are public planning material; daily notes
remain local and are created separately by ``note.py``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
STUDY_DIR = REPO_ROOT / "study"
SCHEDULE_PATH = STUDY_DIR / "schedule.json"
DAYS_DIR = STUDY_DIR / "days"
PLAN_PATH = STUDY_DIR / "DAILY-PLAN.md"
DAY_COUNT = 42
PINNED_OMNI_COMMIT = "870d77446b3fae6e4f4f2a6964f7eae2f75e663a"


def _text(value: Any, default: str = "") -> str:
    if value is None:
        return default
    return str(value).replace("\r\n", "\n").strip() or default


def _cell(value: Any, default: str = "—") -> str:
    """Make a schedule value safe to place in one Markdown table cell."""

    result = _text(value, default).replace("|", "\\|")
    return result.replace("\n", "<br>") or default


def _items(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _number_list(value: Any) -> list[int]:
    numbers: list[int] = []
    for item in _items(value):
        if item is None or item == "":
            continue
        try:
            numbers.append(int(item))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"映射值必须是整数：{item!r}") from exc
    return numbers


def _mapping(value: Any, prefix: str, separator: str = ", ") -> str:
    values = _number_list(value)
    if not values:
        return "—"
    if prefix == "RL-D":
        return separator.join(f"RL-D{number:02d}" for number in values)
    if prefix == "C++-Day":
        return separator.join(f"C++-Day{number:02d}" for number in values)
    if prefix == "K8S-Ch":
        return separator.join(f"K8S-Ch{number:02d}" for number in values)
    return separator.join(f"{prefix}{number:02d}" for number in values)


def _source_lines(sources: Any) -> list[str]:
    lines: list[str] = []
    for source in _items(sources):
        if isinstance(source, dict):
            label = _text(source.get("label") or source.get("title") or source.get("name"))
            url = _text(source.get("url") or source.get("path"))
            if label and url:
                lines.append(f"- [{label}]({url})")
            elif label:
                lines.append(f"- {label}")
            elif url:
                lines.append(f"- {url}")
        elif _text(source):
            lines.append(f"- {_text(source)}")
    return lines or ["- （当天入口待补充）"]


def _evidence_lines(evidence: Any) -> list[str]:
    lines: list[str] = []
    for item in _items(evidence):
        if isinstance(item, dict):
            label = _text(item.get("label") or item.get("title") or item.get("name"))
            url = _text(item.get("url") or item.get("path"))
            if label and url:
                lines.append(f"- [ ] [{label}]({url})")
            elif label:
                lines.append(f"- [ ] {label}")
            elif url:
                lines.append(f"- [ ] {url}")
        elif _text(item):
            lines.append(f"- [ ] {_text(item)}")
    return lines or ["- [ ] （当天证据待补充）"]


def _blocks(day: dict[str, Any]) -> tuple[list[dict[str, Any]], int]:
    raw_blocks = day.get("blocks")
    if not isinstance(raw_blocks, list) or not raw_blocks:
        raise ValueError(f"Day {day.get('day')} 缺少 blocks")
    blocks: list[dict[str, Any]] = []
    total = 0
    for index, raw in enumerate(raw_blocks, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"Day {day.get('day')} 的第 {index} 个 block 不是对象")
        try:
            minutes = int(raw.get("minutes"))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Day {day.get('day')} 的 minutes 无效") from exc
        if minutes <= 0:
            raise ValueError(f"Day {day.get('day')} 的 minutes 必须为正数")
        task = _text(raw.get("task") or raw.get("title"), "待补充")
        blocks.append({"minutes": minutes, "task": task})
        total += minutes
    return blocks, total


def _validate_schedule(schedule: Any) -> list[dict[str, Any]]:
    if not isinstance(schedule, dict) or not isinstance(schedule.get("days"), list):
        raise ValueError("schedule.json 顶层必须包含列表字段 days")
    days = schedule["days"]
    if len(days) != DAY_COUNT:
        raise ValueError(f"schedule.json 应有 {DAY_COUNT} 天，实际为 {len(days)} 天")
    by_number: dict[int, dict[str, Any]] = {}
    for item in days:
        if not isinstance(item, dict):
            raise ValueError("days 中每一项必须是对象")
        try:
            number = int(item.get("day"))
        except (TypeError, ValueError) as exc:
            raise ValueError("每一天必须有整数 day") from exc
        if number in by_number:
            raise ValueError(f"重复的 Day {number}")
        by_number[number] = item
        _blocks(item)
        _number_list(item.get("rl"))
        _number_list(item.get("cpp"))
        _number_list(item.get("k8s"))
    missing = sorted(set(range(1, DAY_COUNT + 1)) - set(by_number))
    if missing:
        raise ValueError(f"缺少学习日：{missing}")
    return [by_number[index] for index in range(1, DAY_COUNT + 1)]


def _write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def _day_navigation(number: int) -> str:
    links = ["[返回 42 天总表](../DAILY-PLAN.md)"]
    if number > 1:
        links.insert(0, f"[← Day {number - 1:02d}](day{number - 1:02d}.md)")
    if number < DAY_COUNT:
        links.append(f"[Day {number + 1:02d} →](day{number + 1:02d}.md)")
    return " · ".join(links)


def _cpp_entry(number: int) -> str:
    path = f"../../../cpp-ai-systems-10days/days/day{number:02d}/README.md"
    return f"C++ Day {number:02d} 工作区路径：`{path}`"


def render_day(day: dict[str, Any]) -> str:
    number = int(day["day"])
    blocks, total = _blocks(day)
    title = _text(day.get("title"), f"学习日 {number}")
    goal = _text(day.get("goal"), "完成当天计划并留下可复核证据")
    status = _text(day.get("status"), "未开始")
    block_rows = ["| 顺序 | 分钟 | 任务 |", "| ---: | ---: | --- |"]
    for index, block in enumerate(blocks, 1):
        block_rows.append(
            f"| {index} | {block['minutes']} | {_cell(block['task'], '待补充')} |"
        )
    block_rows.append(f"| **合计** | **{total}** | **当天学习时间；休息另计** |")

    cpp_values = _number_list(day.get("cpp"))
    cpp_entry_lines = [f"- {_cpp_entry(value)}（本地已有工程入口，不把课程代码重复发布到本计划仓库）" for value in cpp_values]
    if not cpp_entry_lines:
        cpp_entry_lines = ["- 当天没有 C++ 新课；不要重复打开 C++ 课程。"]

    mapping_rows = [
        "| 来源 | 映射 | 用法 |",
        "| --- | --- | --- |",
        f"| RL + Inference 原计划 | {_mapping(day.get('rl'), 'RL-D')} | 复用机制、实验或报告；不重复实现已有证据 |",
        f"| C++ 10 天 | {_mapping(day.get('cpp'), 'C++-Day')} | 只在对应日打开本地课程入口 |",
        f"| K8S AI Infra 大纲 | {_mapping(day.get('k8s'), 'K8S-Ch')} | 作为部署/调度/观测的选读映射，先读概念再看环境 |",
    ]

    source_lines = _source_lines(day.get("sources"))
    evidence_lines = _evidence_lines(day.get("evidence"))
    return "\n".join(
        [
            f"# Day {number:02d} · {title}",
            "",
            f"{_day_navigation(number)}",
            "",
            "> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。",
            "",
            "## 当天概览",
            "",
            "| 项目 | 内容 |",
            "| --- | --- |",
            f"| 状态 | `{status}`（初始状态：全部未开始） |",
            f"| 目标 | {_cell(goal)} |",
            f"| 计划时间 | **{total} 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |",
            "",
            "## 按序安排",
            "",
            *block_rows,
            "",
            "## 当天验收证据",
            "",
            *evidence_lines,
            "",
            "## 与已有工作的复用",
            "",
            _text(day.get("reuse"), "暂无；完成后记录可复用的输入、测试和指标。"),
            "",
            "## 原计划映射",
            "",
            *mapping_rows,
            "",
            "## C++ 本地入口",
            "",
            *cpp_entry_lines,
            "",
            "## 阅读与源码入口",
            "",
            *source_lines,
            "",
            f"- Omni 上游参考（仅相关日适用）：`{PINNED_OMNI_COMMIT}`。",
            "",
            "## 当天笔记",
            "",
            "- [复制每日笔记模板](../templates/daily-note.md)",
            f"- 在仓库根目录运行：`python study/tools/note.py --day {number}`",
            "- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。",
            "",
            _day_navigation(number),
            "",
        ]
    )


def _plan_mapping(day: dict[str, Any]) -> str:
    return " / ".join(
        [
            _mapping(day.get("rl"), "RL-D"),
            _mapping(day.get("cpp"), "C++-Day"),
            _mapping(day.get("k8s"), "K8S-Ch"),
        ]
    )


def render_plan(days: list[dict[str, Any]], schedule: dict[str, Any]) -> str:
    total_minutes = sum(_blocks(day)[1] for day in days)
    updated = _text(schedule.get("updated"), "未注明")
    numbering = _text(schedule.get("day_numbering"), "逻辑学习日；未完成则顺延")
    daily_minutes = _text(schedule.get("daily_minutes"), "按当天安排")
    starting_state = _text(schedule.get("starting_state"), "全部未开始")
    rows = ["| 日 | 主线 | 分钟 | RL / C++ / K8S 映射 | 状态 |", "| ---: | --- | ---: | --- | --- |"]
    for day in days:
        total = _blocks(day)[1]
        rows.append(
            f"| [D{day['day']:02d}](days/day{day['day']:02d}.md) | {_cell(day.get('title'))} | {total} | {_cell(_plan_mapping(day))} | {_cell(day.get('status'), '未开始')} |"
        )
    return "\n".join(
        [
            "# SGLang-Omni / CSE291 / C++ / RL + Inference / K8S · 42 天总表",
            "",
            "> 主线顺序：**D01–D05 先完成 CSE291 → D06 起以 SGLang-Omni 为主线，C++ 在 D06–D15 集中完成 → D16–D26 补推理、K8S 与观测 → D27–D42 完成 RL 闭环、异步系统和一致性分析。**",
            "",
            "## 使用边界",
            "",
            "这些页面是每天的任务卡，不是全套已实现讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock Pipeline 和 C++ 10 天课程已有的可运行例子；其余 Omni、RL、推理和 K8S 内容按固定上游入口读代码、读文档、记录环境，具备 GPU/MPI/多进程/集群条件后再运行。",
            "",
            f"- 日程更新：`{updated}`；编号规则：{numbering}。",
            f"- 时间口径：{daily_minutes}；本表合计 **{total_minutes} 分钟**，休息另计。",
            f"- 起始状态：{starting_state}；当前 42 行状态全部为 **未开始**。",
            "- 前 5 天是 CSE291 PA1/PA2/PA3 的冲刺目标，不把“运行 local_check”当成整份作业完成；测试或必交项未通过就顺延，插入 CSE 补完日，D06 及以后整体顺延。",
            "- 已有证据只复用一次：同一份 MatMul、MPI、推测解码或 benchmark 不为换教材再次重做；后续记录它被复用到哪个 RL/Omni/K8S 概念。",
            f"- SGLang-Omni 上游参考固定 commit：`{PINNED_OMNI_COMMIT}`；上游目录只读。",
            "",
            "## 每天任务",
            "",
            *rows,
            "",
            "## 每天的固定收尾",
            "",
            "1. 打开当天页面，先回答目标问题，再按顺序执行 blocks。",
            "2. 勾选证据；将观察到的事实和自己的解释分开写。",
            "3. 在仓库根目录运行 `python study/tools/note.py --day N`，填写本地笔记；不把 CSE291 解答代码或机器私有日志提交到 GitHub。",
            "4. 如果测试失败，保留失败证据并顺延；不要为了日历上的 Day 编号把状态改成已完成。",
            "",
            "## 目录",
            "",
            "- C++ 10 天课程（工作区路径：`../../cpp-ai-systems-10days/README.md`）",
            "- [RL + Inference 原始 42 天计划](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/curriculum.md)",
            "- [K8S AI Infra 衔接说明](MAPPING.md)",
            "- [每日笔记模板](templates/daily-note.md)",
            "",
        ]
    )


def render_all(schedule_path: Path = SCHEDULE_PATH) -> tuple[int, int]:
    schedule = json.loads(schedule_path.read_text(encoding="utf-8"))
    days = _validate_schedule(schedule)
    changed = 0
    for day in days:
        path = DAYS_DIR / f"day{int(day['day']):02d}.md"
        if _write_if_changed(path, render_day(day)):
            changed += 1
    if _write_if_changed(PLAN_PATH, render_plan(days, schedule)):
        changed += 1
    return len(days), changed


def check_outputs() -> None:
    schedule = json.loads(SCHEDULE_PATH.read_text(encoding="utf-8"))
    days = _validate_schedule(schedule)
    missing = [number for number in range(1, DAY_COUNT + 1) if not (DAYS_DIR / f"day{number:02d}.md").is_file()]
    if missing or not PLAN_PATH.is_file():
        raise ValueError(f"渲染结果缺失：days={missing}, plan={not PLAN_PATH.is_file()}")
    for number, day in enumerate(days, 1):
        content = (DAYS_DIR / f"day{number:02d}.md").read_text(encoding="utf-8")
        total = _blocks(day)[1]
        if f"**{total} 分钟**" not in content:
            raise ValueError(f"Day {number} 的总分钟不匹配")
        if "../templates/daily-note.md" not in content:
            raise ValueError(f"Day {number} 缺少每日笔记模板链接")
        if f"python study/tools/note.py --day {number}" not in content:
            raise ValueError(f"Day {number} 缺少笔记生成命令")
        if number > 1 and f"day{number - 1:02d}.md" not in content:
            raise ValueError(f"Day {number} 缺少前一天链接")
        if number < DAY_COUNT and f"day{number + 1:02d}.md" not in content:
            raise ValueError(f"Day {number} 缺少后一天链接")
    plan = PLAN_PATH.read_text(encoding="utf-8")
    if plan.count("| [D") != DAY_COUNT:
        raise ValueError("总表行数不是 42 行")


def main() -> int:
    parser = argparse.ArgumentParser(description="从 study/schedule.json 渲染 42 天任务卡")
    parser.add_argument("--check", action="store_true", help="只检查已有渲染结果")
    args = parser.parse_args()
    try:
        if args.check:
            check_outputs()
            print("检查通过：42 个日页面、总分钟、前后链接和笔记入口均存在。")
        else:
            count, changed = render_all()
            check_outputs()
            print(f"已检查 {count} 个日页面和总表；更新文件 {changed} 个。")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"渲染失败：{exc}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
