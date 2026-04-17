# 🚀 Advanced Python Port Scanner

A powerful and fast **multi-threaded port scanner** built in Python with support for **banner grabbing**, **service detection**, and **CLI-based customization**.

This tool is designed for **network reconnaissance** and learning purposes in cybersecurity.

---

## 📌 Features

* ⚡ Multi-threaded scanning (fast performance)
* 🔍 Scans custom port ranges
* 🏷️ Basic service detection (common ports)
* 📡 Banner grabbing (identifies running services)
* 🧠 CLI arguments using argparse
* 💾 Save scan results to a file
* 🛠️ Simple and clean output

---

## 🧰 Requirements

* Python 3.x
* No external libraries required (uses built-in modules)

---

## ▶️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/python-port-scanner.git
cd python-port-scanner
```

---

## ⚙️ Usage

```bash
python3 scanner.py <target> [options]
```

---

## 📖 Arguments Explained

| Argument        | Description                      |
| --------------- | -------------------------------- |
| `target`        | Target IP address or domain      |
| `-p, --ports`   | Port range (default: 1-1000)     |
| `-t, --threads` | Number of threads (default: 100) |
| `-o, --output`  | Save results to a file           |

---

## 🧪 Examples

### 🔹 Basic Scan

```bash
python3 scanner.py scanme.nmap.org
```

---

### 🔹 Scan Specific Port Range

```bash
python3 scanner.py scanme.nmap.org -p 1-2000
```

---

### 🔹 Increase Speed (More Threads)

```bash
python3 scanner.py scanme.nmap.org -t 200
```

---

### 🔹 Save Output to File

```bash
python3 scanner.py scanme.nmap.org -o results.txt
```

---

### 🔹 Full Example

```bash
python3 scanner.py scanme.nmap.org -p 1-1000 -t 200 -o scan.txt
```

---

## 🧠 How It Works

1. Takes a target (IP/domain)
2. Scans ports using multi-threading
3. Identifies open ports
4. Attempts banner grabbing
5. Maps common services (HTTP, SSH, etc.)
6. Displays and optionally saves results

---

## 📊 Example Output

```
[+] Port 80 OPEN | Service: HTTP
    Banner: HTTP/1.1 200 OK

[+] Port 22 OPEN | Service: SSH
    Banner: SSH-2.0-OpenSSH_8.2p1 Ubuntu
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.

* Only scan systems you own
* Or have explicit permission to test

Unauthorized scanning is illegal.

---

## 👨‍💻 Author

**Mohamed Jasim**

* Cybersecurity Enthusiast
* Bug Bounty Learner

---

## ⭐ Future Improvements

* TCP SYN scan (Scapy)
* Service version detection
* Colored output
* Progress bar
* OS fingerprinting

---

## 🌟 If you like this project

Give it a ⭐ on GitHub!

