from sub3enum.engines.base import EngineInterface

class FakeEngine(EngineInterface):
    @property
    def name(self):
        return "fake"

    def enumerate(self, domain: str) -> list[str]:
        return [
            f"www.{domain}",
            f"mail.{domain}",
            f"vpn.{domain}"
        ]

