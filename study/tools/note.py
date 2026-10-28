"""Create a non-destructive daily study note from study/schedule.json.

The generated notes are intentionally ignored by ``study/notes/.gitignore``:
the schedule and template are shareable, while filled notes may contain private
experiment output or CSE291 work.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
STUDY_DIR = REPO_ROOT / "study"
TEMPLATE_PATH = STUDY_DIR / "templates" / "daily-note.md"
DEFAULT_SCHEDULE_PATH = STUDY_DIR / "schedule.json"
DEFAULT_OUTPUT_DIR = STUDY_DIR / "notes"
PINNED_OMNI_COMMIT = "870d77446b3fae6e4f4f2a6964f7eae2f75e663a"


def _text(value: Any, fallback: str = "") -> str:
    """Return compact human-readable text for schedule values."""

    if value is None:
        return fallback
    return str(value).replace("\r\n", "\n").strip() or fallback


def _bullet_items(items: Any, empty: str = "- （按当天情况补充）") -> str:
    """Render strings or small schedule objects as Markdown bullets."""

    if not isinstance(items, list) or not items:
        return empty
    rendered: list[str] = []
    for item in items:
        if isinstance(item, dict):
            label = _text(item.get("label") or item.get("title") or item.get("name"))
            url = _text(item.get("url") or item.get("path"))
            if label and url:
                rendered.append(f"- [{label}]({url})")
            elif label:
                rendered.append(f"- {label}")
            elif url:
                rendered.append(f"- {url}")
            else:
                rendered.append("- （未命名条目）")
        else:
            rendered.append(f"- {_text(item, '（空）')}")
    return "\n".join(rendered)


def _render_blocks(blocks: Any) -> str:
    if not isinstance(blocks, list) or not blocks:
        return "- （当天安排尚未细化）"
    rows: list[str] = []
    for block in blocks:
        if isinstance(block, dict):
            minutes = _text(block.get("minutes"), "待定")
            task = _text(block.get("task") or block.get("title"), "待补充")
            rows.append(f"- **{minutes} 分钟**：{task}")
        else:
            rows.append(f"- {_text(block, '待补充')}")
    return "\n".join(rows)


def _find_day(schedule: dict[str, Any], day: int) -> dict[str, Any]:
    days = schedule.get("days")
    if not isinstance(days, list):
        raise ValueError("schedule.json 必须包含列表字段 days")
    for item in days:
        if isinstance(item, dict) and item.get("day") == day:
            return item
    raise ValueError(f"schedule.json 中没有 Day {day} 的安排")


def _relative_day_link(note_path: Path, day: int) -> str:
    target = STUDY_DIR / "days" / f"day{day:02d}.md"
    return Path(__import__("os").path.relpath(target, start=note_path.parent)).as_posix()


def render_note(day: int, item: dict[str, Any], template: str, note_path: Path) -> str:
    title = _text(item.get("title"), f"学习日 {day}")
    replacements = {
        "{{DAY}}": f"{day:02d}",
        "{{TITLE}}": title,
        "{{GOAL}}": _text(item.get("goal"), "完成当天的阅读、运行和证据记录"),
        "{{BLOCKS}}": _render_blocks(item.get("blocks")),
        "{{EVIDENCE}}": _bullet_items(item.get("evidence")),
        "{{REUSE}}": _text(item.get("reuse"), "暂无；完成后写明可复用的输入、测试或指标"),
        "{{SOURCES}}": _bullet_items(item.get("sources"), "- （当天源码或资料入口待补充）"),
        "{{DAY_LINK}}": _relative_day_link(note_path, day),
    }
    rendered = template
    for marker, value in replacements.items():
        rendered = rendered.replace(marker, value)
    return rendered.rstrip() + "\n"


def create_note(
    day: int,
    schedule_path: Path = DEFAULT_SCHEDULE_PATH,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> tuple[Path, bool]:
    """Create a note, returning ``(path, created)`` without overwriting files."""

    if not 1 <= day <= 42:
        raise ValueError("day 必须在 1 到 42 之间")
    if not schedule_path.is_file():
        raise FileNotFoundError(f"找不到学习日程：{schedule_path}")
    try:
        schedule = json.loads(schedule_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"schedule.json 不是有效 JSON：{exc}") from exc
    if not isinstance(schedule, dict):
        raise ValueError("schedule.json 顶层必须是对象")
    item = _find_day(schedule, day)
    if not TEMPLATE_PATH.is_file():
        raise FileNotFoundError(f"找不到笔记模板：{TEMPLATE_PATH}")

    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    note_path = output_dir / f"day{day:02d}.md"
    if note_path.exists():
        return note_path, False

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    rendered = render_note(day, item, template, note_path)
    try:
        # Exclusive creation closes the exists-then-write race when two VS Code
        # tasks request the same day at the same time.
        with note_path.open("x", encoding="utf-8", newline="") as stream:
            stream.write(rendered)
    except FileExistsError:
        return note_path, False
    return note_path, True


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="根据统一日程生成一份每日学习笔记")
    parser.add_argument(
        "--day", type=int, choices=range(1, 43), required=True, metavar="1..42"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="输出目录，默认 study/notes（已存在的笔记不会覆盖）",
    )
    parser.add_argument(
        "--schedule",
        type=Path,
        default=DEFAULT_SCHEDULE_PATH,
        help="日程 JSON；默认 study/schedule.json，便于本地测试",
    )
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        note_path, created = create_note(args.day, args.schedule, args.output_dir)
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"无法生成笔记：{exc}")
        return 2
    if created:
        print(f"已生成：{note_path}")
    else:
        print(f"已存在，未覆盖：{note_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
