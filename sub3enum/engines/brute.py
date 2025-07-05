import re
import dns.resolver
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from sub3enum.engines.base import EngineInterface

class BruteEngine(EngineInterface):
    @property
    def name(self) -> str:
        return "bruteforce"

    def enumerate(self, domain: str) -> list[str]:
        wordlist_path = Path(__file__).parent.parent / "wordlists" / "common.txt"
        if not wordlist_path.exists():
            print("[!] Wordlist not found.")
            return []

        resolver = dns.resolver.Resolver()
        resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
        subdomains = set()

        with wordlist_path.open("r") as f:
            words = [line.strip() for line in f if line.strip()]

        def resolve(word: str) -> str | None:
            sub = f"{word}.{domain}"
            try:
                answers = resolver.resolve(sub, "A")
                return sub if answers else None
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
                return None

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(resolve, word) for word in words]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    subdomains.add(result)

        return list(subdomains)
