
```
███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
████╗  ██║██╔═══██╗██║   ██║██╔══██╗
██╔██╗ ██║██║   ██║██║   ██║███████║
██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝

          >>> NOVA DEVELOPMENT <<<
```

# 🐾 OwO Generator

> **Automated OwO bot command sender for Discord — built by Nova Development.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord)](https://discord.gg/3xjw8snjnB)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Developer](https://img.shields.io/badge/Dev-odinfov-red?style=for-the-badge)](https://github.com/odinfov)

---

## 📖 What is OwO Generator?

**OwO Generator** is a Python-based automation tool that automatically sends OwO bot commands in a specified Discord channel. It handles hunting, selling, cashing out, and coin-flipping — all on autopilot — so you can farm OwO coins and items without lifting a finger.

This tool was developed by **Nova Development** for educational and personal use only.

---

## ✨ Features

- ✅ Auto-sends `owo hunt` to hunt animals
- ✅ Auto-sends `owo h` (shorthand hunt)
- ✅ Auto-sends `owo sell all` to sell collected items
- ✅ Auto-sends `owo cash` to collect rewards
- ✅ Auto-sends `owo cf 2500 h` / `owo cf 2500 t` to coinflip
- ✅ Supports **multiple Discord tokens** for faster generation
- ✅ Random sleep intervals (15–20 seconds) to avoid rate limits and detection
- ✅ Logs sent messages to console with account info
- ✅ Webhook logging for token verification

---

## 📋 Requirements

Make sure you have the following installed before running:

| Requirement | Version |
|---|---|
| Python | 3.8 or higher |
| `requests` library | Latest |

Install dependencies with:

```bash
pip install requests
```

---

## ⚙️ Setup & Configuration

### Step 1 — Clone or Download the Project

```bash
git clone https://github.com/YourUsername/OwO-Generator.git
cd OwO-Generator
```

Or simply download and extract the ZIP file.

---

### Step 2 — Add Your Discord Token(s)

Open `main.py` and fill in your Discord account token(s):

```python
tokens = ["YOUR_DISCORD_TOKEN_HERE"]  # Add more tokens for faster gen
```

> ⚠️ **You can add multiple tokens** for parallel generation:
> ```python
> tokens = ["TOKEN1", "TOKEN2", "TOKEN3"]
> ```

---

### Step 3 — Set Your Channel ID

In `main.py`, set the Discord channel ID where OwO commands should be sent:

```python
channelid = "YOUR_CHANNEL_ID_HERE"
```

> 💡 **How to get Channel ID:**
> 1. Open Discord
> 2. Go to `Settings → Advanced → Enable Developer Mode`
> 3. Right-click on the channel → `Copy ID`

---

### Step 4 — Run the Bot

```bash
python main.py
```

The bot will start, verify your tokens, and begin sending OwO commands automatically!

---

## 📁 Project Structure

```
OwO-Generator/
│
├── main.py          # Main entry point — configure tokens & channel ID here
│
└── data/
    └── cogs.py      # Token validator and webhook logger
```

---

## 🖥️ How It Works

1. **Token Verification** — On startup, `cogs.py` verifies each token by hitting the Discord API and logs the result.
2. **Command Loop** — The main loop continuously sends the following OwO commands in order:
   - `owo h` — Hunt animals
   - `owo sell all` — Sell all collected animals
   - `owo cash` — Cash out gems/rewards
   - `owo hunt` — Extended hunt command
   - `owo cf 2500 h` — Coinflip heads with 2500 coins
   - `owo cf 2500 t` — Coinflip tails with 2500 coins
3. **Random Delay** — Waits a random 15–20 seconds between each cycle to mimic human behavior.

---

## ⚠️ Disclaimer

> **This tool is made for educational purposes only.**
>
> - Using self-bots or automation tools on Discord **may violate Discord's Terms of Service**.
> - The developer (**Nova Development**) is **not responsible** for any bans, suspensions, or other consequences resulting from the use of this tool.
> - Use at your own risk.

---

## 🔒 Privacy Policy

**Nova Development** takes your privacy seriously.

- We **do not collect**, store, or share your Discord tokens with any third party.
- Token verification is done locally on your machine.
- Webhook logging is used solely for internal diagnostic purposes and is **only visible to the developer**.
- No personal data is transmitted to any external server other than Discord's official API endpoints.
- By using this tool, you agree that you are solely responsible for how you use it.

---

## 📜 Terms of Use

By downloading and using **OwO Generator**, you agree to the following:

1. You will **not** use this tool to harm, harass, or disrupt other Discord users.
2. You acknowledge that this tool may violate Discord's Terms of Service and you accept all associated risks.
3. You will **not** redistribute or resell this tool without permission from Nova Development.
4. Nova Development reserves the right to update or discontinue this project at any time.

---

## 🤝 Support & Community

Have questions, suggestions, or issues? Join our community!

<div align="center">

### 🔗 Follow & Connect

[![Discord Server](https://img.shields.io/badge/Join_Discord_Server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/3xjw8snjnB)
[![GitHub](https://img.shields.io/badge/GitHub-odinfov-181717?style=for-the-badge&logo=github)](https://github.com/odinfov/OwO-Generator-SRC-)

</div>

> 📌 **Discord Server:** [discord.gg/3xjw8snjnB](https://discord.gg/3xjw8snjnB) — Get support, report bugs, and stay updated on new releases.
>
> 📦 **GitHub Repository:** [github.com/odinfov/OwO-Generator-SRC-](https://github.com/odinfov/OwO-Generator-SRC-.git)

---

## 👨‍💻 Developer

<div align="center">

| | |
|---|---|
| **Owner** | Odin (`odinfov`) |
| **Project** | OwO Generator |
| **Language** | Python 3.8+ |
| **Version** | 1.0.0 |
| **GitHub** | [github.com/odinfov](https://github.com/odinfov) |
| **Support** | [discord.gg/novadevelopment](https://discord.gg/3xjw8snjnB) |

</div>

---

<div align="center">

**Made with ❤️ by Odin (odinfov)**

*If you found this useful, consider giving it a ⭐ on GitHub!*

</div>
