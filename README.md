# Cam-Tool 👁️🌍

Cam-Tool is a Python-based command-line utility that fetches and displays publicly available IP camera streams indexed by country.  
It features a colorful terminal UI, loading animations, and an interactive country selector.

> ⚠️ **Disclaimer**:  
> This tool is intended **for educational and research purposes only**.  
> It only accesses **publicly indexed cameras** available on the internet.  
> The author is **not responsible** for any misuse of this tool.  
> Always respect privacy laws and regulations in your country.

---

## ✨ Features

- 🌐 Browse public IP cameras **by country**
- 🎨 Colorful terminal interface with animations
- ⏳ Loading & typing effects for better UX
- 🆔 Generates a local unique user ID (non-identifiable)
- 📡 Automatically fetches your public IP
- 📱 Works on **Linux**, **macOS**, **Windows**, and **Termux**
- 🔁 Restart-friendly loop system

---

## 📸 Data Source

This tool retrieves data from:

- **Insecam** – a public index of open IP cameras  
  (No authentication, no hacking, no bypassing security)

---

## 🛠️ Requirements

- Python **3.7+**
- Internet connection

### Python Libraries
The script will auto-install missing dependencies:
- `requests`
- `colorama`

---

## 🚀 Installation

```bash
git clone https://github.com/code406org-alt/cam-tool.git
cd cam-tool
python cam-tool.py
