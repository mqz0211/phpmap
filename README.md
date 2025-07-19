# phpmap

**phpmap** is a modular PHP vulnerability scanner and exploitation framework. Inspired by `sqlmap`, this tool targets PHP-specific attack vectors like:

- 🔍 Local File Inclusion (LFI)
- 📂 Upload Bypass (soon)
- 🧬 PHP Deserialization Exploits (soon)

---

## 🚀 Features

- Automated LFI scanner
- Clean CLI interface
- Easily extendable module-based architecture
- Debian-packaging ready for Kali Linux integration
- Lightweight Python3-based utility

---

## 🧪 Usage

```bash
python3 phpmap.py -u http://target.com/index.php --lfi
