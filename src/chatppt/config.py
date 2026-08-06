"Typed environment configuration for ChatPPT."

from chatenv import BaseEnvConfig, EnvField


class ChatpptConfig(BaseEnvConfig):
    "ChatPPT ChatEnv configuration."

    _title = "ChatPPT Configuration"
    _aliases = ["chatppt"]
    _storage_dir = "Chatppt"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATPPT_API_KEY = EnvField(
        "CHATPPT_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatpptConfig"]
