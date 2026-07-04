from pathlib import Path


CORE_DOCS = (
    Path("README.md"),
    Path("docs/architecture.md"),
    Path("docs/compression_policies.md"),
    Path("docs/evaluation.md"),
)
RESEARCH_DOC = Path("docs/kv_cache_research.md")
RUNTIME_ROOT = Path("zip_agent")


def test_current_docs_surface_keeps_existing_product_policies() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    policies = Path("docs/compression_policies.md").read_text(encoding="utf-8")

    for policy in ("baseline", "linguaroom", "headroom", "rtk", "caveman", "zip-auto"):
        assert f"`{policy}`" in readme
        assert f"## {policy}" in policies

    architecture = Path("docs/architecture.md").read_text(encoding="utf-8")
    for stage in ("LinguaRoom", "Headroom", "RTK", "Guarded Caveman"):
        assert stage in architecture


def test_kv_cache_is_research_only() -> None:
    research_text = RESEARCH_DOC.read_text(encoding="utf-8")

    assert "KV-cache compression is a separate research track" in research_text
    assert "not part of the core Z.I.P. runtime path" in research_text
    assert "Promotion criteria" in research_text

    for doc_path in CORE_DOCS:
        doc_text = doc_path.read_text(encoding="utf-8")
        assert "KV-cache" in doc_text
        assert "research track" in doc_text
        assert "KV-cache compression policy" not in doc_text

    for runtime_path in RUNTIME_ROOT.rglob("*.py"):
        runtime_text = runtime_path.read_text(encoding="utf-8")
        assert "KV-cache" not in runtime_text
        assert "kv_cache" not in runtime_text.lower()
