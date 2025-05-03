import argparse
import requests
from urllib.parse import urljoin

def get_args():
    parser = argparse.ArgumentParser(description="Directory brute-forcer")
    parser.add_argument('-u','--url',required=True, help="Target URL (e.g. http://10.10.37.64/)")
    parser.add_argument('-w','--wordlist',required=True, help = "Path to wordlist file")
    parser.add_argument('-v','--verbose',action="store_true",help="Show all status codes")
    return parser.parse_args()

MAGENTA = "\033[95m"
RESET = "\033[0m"

def print_banner():
    banner=r"""
 __             __    ___________     _    __
 \ \           / /   |  _________|   | |  / /
  \ \         / /    | |             | | / /
   \ \       / /     | |_________    | |/ /
    \ \     / /      |_________  |   |   \
     \ \   / /                 | |   | |\ \  
      \ \_/ /         _________| |   | | \ \
       \___/         |___________|   |_|  \_\

       VSK - VeilSeek 1.0

    """
    print(MAGENTA + banner + RESET)
def brute_force(url,wordlist_path,verbose=False):
    try:
        with open(wordlist_path,'r') as f:
            paths= f.read().splitlines()
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist_path}")
        return
    
    print(f"\n[~] Starting scan on: {url}")

    for path in paths:
        full_url = urljoin(url,path)
        try:
            response = requests.get(full_url,timeout=5)
            if response.status_code==200:
                print(f"[+] Found: {full_url} [200 OK]")
            elif verbose:
                print(f"[-] {full_url} [{response.status_code}]")
        except requests.RequestException:
            continue


if __name__ == "__main__":
    print_banner()
    args = get_args()
    brute_force(args.url,args.wordlist,args.verbose)





