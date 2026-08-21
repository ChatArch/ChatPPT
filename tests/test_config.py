from chatenv.store import EnvStore

from chatppt.config import ChatpptConfig


def test_chatppt_provider_uses_typed_sensitive_profile_storage(tmp_path):
    fields = ChatpptConfig.get_fields()
    store = EnvStore(tmp_path)

    profile_path = store.save_profile(
        ChatpptConfig,
        "work",
        {"CHATPPT_API_KEY": "profile-secret"},
    )

    assert ChatpptConfig._aliases == ["chatppt"]
    assert fields["CHATPPT_API_KEY"].is_sensitive is True
    assert store.active_path(ChatpptConfig) == tmp_path / "Chatppt" / ".env"
    assert profile_path == tmp_path / "Chatppt" / "work.env"
    assert store.load_profile(ChatpptConfig, "work") == {
        "CHATPPT_API_KEY": "profile-secret"
    }
