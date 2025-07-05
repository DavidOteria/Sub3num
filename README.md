# sub3num

**sub3num** is a modular subdomain enumeration library written in Python.  
It provides both passive and active subdomain discovery engines and is designed to be integrated into larger OSINT tools.

---

## Features

- Passive enumeration via `crt.sh`
- Active bruteforce DNS engine with multi-threading
- Custom DNS resolver support
- Deduplication and sorting of results
- Easy export to `.txt`
- Designed for integration and reusability

---

## Structure 
```cpp
sub3enum/
├── engines/
│   ├── crtsh.py
│   ├── brute.py
│   └── base.py
├── utils/
│   └── export.py
├── enumerator.py
├── wordlists/
│   └── common.txt
```

## Installation

### Option 1 – via GitHub

```bash
pip install git+https://github.com/DavidOteria/sub3num.git
```

### Option 2 – clone and dev mode 

```bash
git clone https://github.com/DavidOteria/sub3num.git
cd sub3num
pip install -e .
```

## Usage exemples 

```python
from sub3enum.engines.crtsh import CrtShEngine
from sub3enum.engines.brute import BruteEngine
from sub3enum.enumerator import SubdomainEnumerator

domain = "example.com"
engines = [CrtShEngine(), BruteEngine()]

scanner = SubdomainEnumerator(domain, engines)
scanner.run()

results = scanner.get_results()
for sub in results:
    print(sub)
```

## Requirements 

```bash 
pip install -r requirements.txt 
```


