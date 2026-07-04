from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Final, NamedTuple


COMMAND_NAMES: Final = ("zip-save", "zip-benchmark", "zip-verify")
SURFACE_ROOTS: Final = (Path("commands"), Path("claude/commands"), Path("hermes/commands"))
SKILL_PATH: Final = Path("skills/zip-token-saver/SKILL.md")
HERMES_AGENT_PATH: Final = Path("hermes/HERMES_AGENT.md")


class CommandSurface(NamedTuple):
    command_name: str
    local_path: Path
    claude_path: Path
    hermes_path: Path


COMMAND_SURFACES: Final = tuple(
    CommandSurface(
        command_name=command_name,
        local_path=Path("commands") / f"{command_name}.md",
        claude_path=Path("claude/commands") / f"{command_name}.md",
        hermes_path=Path("hermes/commands") / f"{command_name}.md",
    )
    for command_name in COMMAND_NAMES
)


def test_packaging_surface_files_are_discoverable() -> None:
    for command_name in COMMAND_NAMES:
        for surface_root in SURFACE_ROOTS:
            path = surface_root / f"{command_name}.md"

            text = path.read_text(encoding="utf-8")

            assert text.startswith("#")
            assert command_name in text

    skill_text = SKILL_PATH.read_text(encoding="utf-8")
    hermes_text = HERMES_AGENT_PATH.read_text(encoding="utf-8")

    assert "zip-token-saver" in skill_text
    assert "Hermes Z.I.P. Agent" in hermes_text


def test_command_mirror_parity() -> None:
    for surface in COMMAND_SURFACES:
        expected_paths = (
            surface.local_path.as_posix(),
            surface.claude_path.as_posix(),
            surface.hermes_path.as_posix(),
            SKILL_PATH.as_posix(),
        )

        for path in (surface.local_path, surface.claude_path, surface.hermes_path):
            text = path.read_text(encoding="utf-8")

            assert "Mirror parity:" in text
            assert f"Canonical command: `{surface.command_name}`" in text
            for expected_path in expected_paths:
                assert f"`{expected_path}`" in text


def test_skill_and_hermes_agent_list_all_command_surfaces() -> None:
    packaging_text = "\n".join(
        (
            SKILL_PATH.read_text(encoding="utf-8"),
            HERMES_AGENT_PATH.read_text(encoding="utf-8"),
        )
    )

    for surface in COMMAND_SURFACES:
        assert f"`{surface.local_path.as_posix()}`" in packaging_text
        assert f"`{surface.claude_path.as_posix()}`" in packaging_text
        assert f"`{surface.hermes_path.as_posix()}`" in packaging_text


def test_cli_help_lists_packaging_entrypoints() -> None:
    result = subprocess.run(
        (sys.executable, "-m", "zip_agent.cli", "--help"),
        check=True,
        capture_output=True,
        text=True,
    )

    assert "benchmark" in result.stdout
    assert "save" in result.stdout
    assert "verify" in result.stdout
