import requests
import re
from sub3enum.engines.base import EngineInterface

class CrtShEngine (EngineInterface): 
    @property 
    def name(self) -> str: 
        return "crtsh" 
    
    def enumerate (self, domain: str) -> list[str]:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"

        try:
            response = requests.get(url, timeout=30)
            if response.status_code != 200:
                return []
        
            data = response.json()
            subdomains = set() 

            for entry in data: 
                name = entry.get("name_value", "")
                matches = re.findall(rf"[\w.-]+\.{re.escape(domain)}", name)
                subdomains.update(matches)

            return list(subdomains)
        
        except Exception as e:
            print(f"[!] {self.name} error: {e}")
            return []
    