# VeilSeek

VeilSeek is a minimal Python-based directory brute-forcer written for security testing and CTFs.

## Features

- Fast and lightweight
- Verbose mode to view all HTTP responses
- Custom wordlist support
- Colorful CLI banner

## Requirements

- Python 3.x
- `requests` library

Install with:
```pip install -r requirements.txt```

## Usage

```python3 v1.py -u <target_url> -w <wordlist_path> [-v]```

## Arguments:

    -u, --url – Target URL (e.g., http://10.10.10.10/)

    -w, --wordlist – Path to wordlist file

    -v, --verbose – Show all status codes

Example:

```python3 v1.py -u http://10.10.10.10/ -w wordlist.txt -v```

Disclaimer

This tool is for educational and authorized testing purposes only.

