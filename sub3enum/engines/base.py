from abc import ABC, abstractmethod

class EngineInterface(ABC): 
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the engine."""
        pass

    @abstractmethod
    def enumerate(self, domain: str) -> list[str]:
        """Enumerate subdomains for the given target."""
        pass