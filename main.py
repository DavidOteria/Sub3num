from sub3enum.enumerator import SubdomainEnumerator
from sub3enum.engines.crtsh import CrtShEngine
from sub3enum.engines.brute import BruteEngine
from sub3enum.utils.export import export_to_txt


def main():

    domain = input("Enter the domain to enumerate subdomains for : ") 

    if not domain: 
        print("Domain cannot be empty.")
        return 
    
    engines = [
        CrtShEngine(),
        BruteEngine()
        ]
    scanner = SubdomainEnumerator(domain, engines)

    scanner.run()

    results = sorted(scanner.get_results())
    print(f"\n [+] Found {len(results)} unique subdomains:")
    for subdomain in results:
        print(f" - {subdomain}")

    output_path = export_to_txt(results, domain)
    print(f"\n[+] Résultats exportés vers : {output_path}")

if __name__ == "__main__":
     main()
