# phpmap

**phpmap** is a modular PHP vulnerability scanner and exploitation framework, designed to automate the discovery of common PHP-based web application flaws. Inspired by `sqlmap`, `phpmap` targets vulnerabilities like Local File Inclusion (LFI), Remote File Inclusion (RFI), upload bypasses, and PHP deserialization bugs.

phpmap is designed with modularity and ethical testing in mind and aims to meet Kali Linux packaging standards.

---

## Features

- Local File Inclusion (LFI) scanner
- Remote File Inclusion (RFI) scanner
- SQL Injection scanner
- XSS scanner
- Directory listing checker
- Backup/config file finder
- Admin panel bruteforcer
- phpinfo() exposure checker
- Upload bypass (coming soon)
- PHP deserialization (coming soon)

## Example Usage

```bash
python3 phpmap.py -u http://example.com/index.php --lfi
python3 phpmap.py -u http://example.com/index.php --sql-injection
```
---
Available options:

```bash
-u, --url              Target URL
--lfi                  Run LFI scanner
--upload-bypass        Scan for file upload bypasses (soon)
--deserialization      Scan for PHP deserialization flaws (soon)
```

---

## Installation

```bash
git clone https://github.com/mqz0211/phpmap.git
cd phpmap
pip install -r requirements.txt
chmod +x phpmap.py
```

---

## Run From Anywhere (Optional)

To run `phpmap` from anywhere on your system:

```bash
sudo cp phpmap.py /usr/local/bin/phpmap
```

Then simply run:

```bash
phpmap -u http://target.com/index.php --lfi
```

---

## Open in Cloud Shell

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/mqz0211/phpmap&cloudshell_working_dir=phpmap)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mqz0211/phpmap)

[![Run on Replit](https://replit.com/badge/github/mqz0211/recoverycodegencli)](https://replit.com/new/github.com/mqz0211/phpmap)

[![Open in Codespaces](https://img.shields.io/badge/Open%20in%20-GitHub%20Codespaces-blue?logo=github)](https://github.com/codespaces/new?template_repository=github.com/mqz0211/phpmap)

[![Run on Ideone](https://img.shields.io/badge/Run%20on-Ideone-orange?logo=codeforces)](https://ideone.com/)

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

## Author

Developed by **MQZ**
GitHub: [github.com/mqz0211](https://github.com/mqz0211)

---

## Dependencies

* Python 3.6+
* `requests` (to be used in active modules)

---

## Contributing

Pull requests and module contributions are welcome. If you want to add new scanners (e.g. eval injection, RCE, etc.), open an issue first.

---

## Disclaimer

This tool is for **educational and authorized testing purposes only**. Any misuse is the sole responsibility of the user. The author assumes no liability.

---

## Upcoming Modules

* `--rfi` (Remote File Inclusion)
* `--php-self-injection`
* `--eval-check`
* `--log-poisoning`
* Payload encoder / WAF bypass

---

## Copyright

```
Copyright © 2025 Qhaleesh Zhariif

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This project is released in good faith for educational and ethical testing purposes only.
The developer shall not be held liable for any misuse or damage resulting from this software,
including violations of laws in any jurisdiction, including Malaysia.
It is the end user's responsibility to ensure lawful usage and compliance with all applicable regulations.
```
