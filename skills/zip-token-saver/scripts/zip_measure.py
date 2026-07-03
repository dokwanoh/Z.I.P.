from __future__ import annotations

import sys

from zip_agent.core.tokenizer import estimate_tokens


def main() -> int:
    text = sys.stdin.read()
    print(estimate_tokens(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
