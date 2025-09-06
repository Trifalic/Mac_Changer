# MAC\_Changer

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple Python tool to view and change your MAC address on Linux systems. Perfect for testing network security, privacy, or just messing around like a hacker.

---

## 🔥 Features

* Get your current MAC address using `ip link`.
* Generate a random valid MAC address.
* Change your MAC address on the fly.
* Simple, lightweight, and easy to use.

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/Trifalic/Mac_Changer.git
cd Mac_Changer
```

2. Install dependencies (if not already installed):

```bash
pip install -r requirements.txt
```

*(Note: This script uses standard Python libraries like `subprocess`, `re`, and `random`. If you don’t have `pip` dependencies, you can skip this.)*

---

## ⚡ Usage

```bash
python mac_changer.py --interface eth0
```

**Steps:**

1. **Check current MAC:**

   ```bash
   python mac_changer.py --get
   ```

2. **Change MAC to a random one:**

   ```bash
   python mac_changer.py --random
   ```

3. **Change MAC to a specific one:**

   ```bash
   python mac_changer.py --set 00:11:22:33:44:55
   ```

---

## 💡 How it Works

* Uses Python’s `subprocess` to run Linux `ip link` commands.
* Uses regex to capture the current MAC address.
* Generates random MAC addresses using Python’s `random` and `string` modules.

**Example:**

```python
mac_search.group(1)  # Extracts only the MAC address from ip link output
```

---

## ⚠️ Important Notes

* Only works on **Linux systems**.
* Requires **root privileges** to change MAC addresses:

  ```bash
  sudo python mac_changer.py --random
  ```
* Misusing MAC address changes can break your network connection. Use responsibly.

---

## 📂 Repository Link

[https://github.com/Trifalic/Mac\_Changer](https://github.com/Trifalic/Mac_Changer)

---

## 📝 License

MIT License. Free to use, modify, and share.
