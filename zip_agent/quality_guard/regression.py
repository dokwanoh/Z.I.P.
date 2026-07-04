from __future__ import annotations

import re
from typing import Final, Iterable

from zip_agent.core.schemas import BenchmarkTask

ACCEPTANCE_LINE_RE: Final = re.compile(r"^`?acceptance`?\s*:", re.IGNORECASE)
PATH_RE: Final = re.compile(r"[A-Za-z_][A-Za-z0-9_-]*(?:[./][A-Za-z0-9_-]+)+")
IDENTIFIER_RE: Final = re.compile(r"[A-Za-z_][A-Za-z0-9_]*_[A-Za-z0-9_]*")
TERM_RE: Final = re.compile(
    r"`(?P<quoted>[^`]+)`|"
    rf"(?P<path>{PATH_RE.pattern})|"
    rf"(?P<identifier>{IDENTIFIER_RE.pattern})"
)


def required_terms(task: BenchmarkTask) -> tuple[str, ...]:
    terms = list(_terms_from_text(task.expected_behavior))
    terms.extend(_terms_from_text(task.repo_context))
    return _dedupe(terms)


def missing_required_terms(task: BenchmarkTask, actual: str) -> tuple[str, ...]:
    actual_lower = actual.lower()
    required = required_terms(task)
    return tuple(term for term in required if term.lower() not in actual_lower)


def missing_acceptance_terms(task: BenchmarkTask, actual: str) -> tuple[str, ...]:
    actual_lower = actual.lower()
    required: list[str] = []
    for line in task.repo_context.splitlines():
        stripped = line.strip()
        if ACCEPTANCE_LINE_RE.match(stripped):
            _, terms = stripped.split(":", maxsplit=1)
            required.extend(_terms_from_text(terms))
    return tuple(term for term in _dedupe(required) if term.lower() not in actual_lower)


def _terms_from_text(text: str) -> list[str]:
    terms: list[str] = []
    for match in TERM_RE.finditer(text):
        term = _matched_term(match)
        if term != "":
            terms.append(term)
    return terms


def _matched_term(match: re.Match[str]) -> str:
    quoted = match.group("quoted")
    if quoted is not None:
        term = quoted.strip()
        if _is_required_term(term):
            return term
        return ""
    path = match.group("path")
    if path is not None:
        return path.strip(".,:;")
    identifier = match.group("identifier")
    if identifier is not None:
        return identifier.strip(".,:;")
    return ""


def _is_required_term(term: str) -> bool:
    cleaned = term.strip("`.,:;")
    return PATH_RE.fullmatch(cleaned) is not None or IDENTIFIER_RE.fullmatch(cleaned) is not None


def _dedupe(items: Iterable[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            ordered.append(item)
            seen.add(item)
    return tuple(ordered)
