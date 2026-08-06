from pathlib import Path


def test_publish_workflow_is_tag_only_and_guard_is_unconditional():
    text = Path(".github/workflows/publish.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch" not in text
    assert "tags:" in text
    assert '"v*"' in text

    guard_section = text.split("- name: Check tag matches package version", 1)[1]
    guard_section = guard_section.split("- name:", 1)[0]
    assert "github.event_name" not in guard_section
    assert "if:" not in guard_section
    assert "GITHUB_REF_NAME" in guard_section
    assert "RELEASE_TAG" in guard_section
