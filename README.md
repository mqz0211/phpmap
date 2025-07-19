# phpmap

**phpmap** is a modular PHP vulnerability scanner and exploitation framework, designed to automate the discovery of common PHP-based web application flaws. Inspired by `sqlmap`, `phpmap` targets vulnerabilities like Local File Inclusion (LFI), Remote File Inclusion (RFI), upload bypasses, and PHP deserialization bugs.

---

## 🚀 Features

* 🔍 Local File Inclusion (LFI) Scanner
* 📂 Upload Bypass Detection *(coming soon)*
* 🧬 PHP Deserialization Exploit Scanner *(coming soon)*
* 🧰 Modular code for easy extension
* 🎯 CLI-based and fast
* 🐧 Kali Linux ready (Debian packaging supported)

---

## 🧪 Example Usage

```bash
python3 phpmap.py -u http://target.com/index.php --lfi
```

Available options:

```bash
-u, --url              Target URL
--lfi                  Run LFI scanner
--upload-bypass        Scan for file upload bypasses (soon)
--deserialization      Scan for PHP deserialization flaws (soon)
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/phpmap.git
cd phpmap
pip install -r requirements.txt
```

---

## 📜 License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

## 👨‍💻 Author

Developed by **Your Name / Alias**
GitHub: [github.com/yourusername](https://github.com/yourusername)
Twitter: [@yourhandle](https://twitter.com/yourhandle)

---

## 🛠 Dependencies

* Python 3.6+
* `requests` (to be used in active modules)

---

## 🤝 Contributing

Pull requests and module contributions are welcome. If you want to add new scanners (e.g. eval injection, RCE, etc.), open an issue first.

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**. Any misuse is the sole responsibility of the user. The author assumes no liability.

---

## 🔥 Upcoming Modules

* `--rfi` (Remote File Inclusion)
* `--php-self-injection`
* `--eval-check`
* `--log-poisoning`
* Payload encoder / WAF bypass
