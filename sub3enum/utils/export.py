from pathlib import Path

def export_to_txt(subdomains: list[str], domain: str, output_dir: str = "results") -> str:
    """
    Export list of subdomains to a text file.

    :param subdomains: List of subdomains to write
    :param domain: Target domain (e.g., bnp.fr)
    :param output_dir: Folder where to save results
    :return: Path to the exported file
    """
    Path(output_dir).mkdir(exist_ok=True)
    output_path = Path(output_dir) / f"{domain}_subdomains.txt"

    with output_path.open("w", encoding="utf-8") as f:
        for sub in subdomains:
            f.write(sub + "\n")

    return str(output_path)
