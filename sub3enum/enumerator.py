from sub3enum.engines.base import EngineInterface

class SubdomainEnumerator:
    """
    A class to enumerate subdomains using various engines.
    """
    def __init__(self, domain: str, engines: list[EngineInterface]):
        """
        Initialize the enumerator with a target domain and a list of engines.
        
        :param domain: The target domain to enumerate subdomains for.
        :param engines: A list of EngineInterface implementations to use for enumeration.
        :param engines: List of engines to use for subdomain enumeration.
        """
        self.domain = domain
        self.engines = engines
        self.results = set()

    def run(self):
        """
        Run the enumeration process using all specified engines.
        """
        for engine in self.engines:
            print(f"[+] Running : {engine.name}")
            try: 
                subdomains = engine.enumerate(self.domain)
                self.results.update(subdomains)
                print(f"[+] Found {len(subdomains)} subdomains using {engine.name}")
            except Exception as e: 
                print(f"[-] Error with {engine.name}: {e}")
        
    def get_results(self) -> set[str]:
        """
        Get the unique subdomains found during enumeration.
        
        :return: A set of unique subdomains.
        """
        return self.results