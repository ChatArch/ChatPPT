from pathlib import Path


def test_publish_workflow_is_tag_only_and_guard_is_unconditional():
    text = Path(".github/workflows/publish.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch" not in text
    assert "tags:" in text
    assert '"v*"' in text
    assert "Ensure tag commit is on default branch" in text
    assert "git merge-base --is-ancestor" in text
    assert "refs/remotes/origin/main" in text

    guard_section = text.split("- name: Check tag matches package version", 1)[1]
    guard_section = guard_section.split("- name:", 1)[0]
    assert "github.event_name" not in guard_section
    assert "if:" not in guard_section
    assert "GITHUB_REF_NAME" in guard_section
    assert "RELEASE_TAG" in guard_section


def test_ci_verifies_supported_versions_and_installed_package_contracts():
    text = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert 'python-version: ["3.10", "3.11", "3.12"]' in text
    assert "chatppt --version" in text
    assert "chatppt --tree" in text
    assert "chatppt --tree-brief" in text
    assert "python -m twine check dist/*" in text
    assert "chatppt-wheel/bin/chatppt" in text
    assert "chatppt-wheel/bin/chatenv" in text
    assert "mkdocs build --strict" in text
