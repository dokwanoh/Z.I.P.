from __future__ import annotations

import ast
from typing import List


def python_outline(source: str) -> str:
    tree = ast.parse(source)
    rows: List[str] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            rows.append(f"def {node.name}({', '.join(arg.arg for arg in node.args.args)})")
        elif isinstance(node, ast.ClassDef):
            rows.append(f"class {node.name}")
    return "\n".join(rows)
