from __future__ import annotations

import re

TOKEN_RE = re.compile(r"[A-Za-z0-9_./:-]+|[가-힣]+|[^\s]")


def estimate_tokens(text: str) -> int:
    if text.strip() == "":
        return 0
    tokens = 0
    for match in TOKEN_RE.finditer(text):
        piece = match.group(0)
        tokens += _piece_cost(piece)
    return tokens


def _piece_cost(piece: str) -> int:
    if re.fullmatch(r"[가-힣]+", piece) is not None:
        return max(1, (len(piece) + 1) // 2)
    if re.fullmatch(r"[A-Za-z0-9_./:-]+", piece) is not None:
        return max(1, (len(piece) + 3) // 4)
    return 1
