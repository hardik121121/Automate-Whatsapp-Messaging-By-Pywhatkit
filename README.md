# 🤖 WhatsApp Automation Script 📱

## 📖 Overview
This Python script automates the process of sending WhatsApp messages using the `pywhatkit` library. You can schedule messages to be sent at a specific time in the future—perfect for reminders, notifications, or just for fun! 🎉

## ✨ Features
- 🌐 Automatically opens WhatsApp Web in your default browser.
- ⏰ Schedules and sends messages to a specific phone number at a given time.
- 📝 Customizable messages for multiple contacts and times.
- 📅 Simple and easy-to-use scheduling for WhatsApp automation.

## 🛠 Requirements
Before you start, make sure you have the following:
- 💻 Python 3.x installed on your computer. (Download from [python.org](https://www.python.org/downloads/))
- 📦 `pywhatkit` library. Install it via pip.
- 🌍 An active internet connection.
- 📲 WhatsApp account linked to WhatsApp Web.

## 🚀 Installation

### 1️⃣ Install Python 3.x
If you don't have Python installed yet, download and install it from [python.org](https://www.python.org/downloads/).

### 2️⃣ Install the required Python library
After installing Python, open your terminal or command prompt and install `pywhatkit` by running:

```bash
pip install pywhatkit
```

### 3️⃣ Setup WhatsApp Web
- Open WhatsApp Web in your default browser.
- If it's your first time, you'll need to scan the QR code using the WhatsApp mobile app to link your account.

## 📜 Usage

### 1️⃣ Clone or Download the repository


Or, download the zip file and extract it.

### 2️⃣ Modify the Script
Open the `App.py` file and make sure to update the following parameters:
- **Recipient's Phone Number**: Replace the placeholder `+917488343926` with the recipient's WhatsApp number.
- **Message**: Change the message text to whatever you'd like to send.

Example:
```python
pywhatkit.sendwhatmsg("+917488343926", "Hello! This is an automated WhatsApp message sent by my bot 🤖", 17, 46)
```

### 3️⃣ Run the Script
Once you're ready, run the Python script using the following command:

```bash
python App.py
```

The script will:
- Open WhatsApp Web in your default browser 🌐.
- Wait for the scheduled time ⏰ (at least 1-2 minutes in advance).
- Automatically send the message to the provided contact 📲.

## ⚙️ Customizing the Delay
You can adjust the delay time for sending the messages by modifying the time parameters in the script. For example:
- `17` (hour)
- `46` (minute)

Make sure that the time is set to a future value (1-2 minutes ahead) for the script to work properly. ⏳

## 💬 Example

```python
# Sends a message to the number +917488343926 at 5:46 PM
pywhatkit.sendwhatmsg("+917488343926", "Don't Worry Bhai! This is an automated WhatsApp message. 📱", 17, 46)

# Sends another message at 5:47 PM
pywhatkit.sendwhatmsg("+917488343926", "If you received this, it means the bot is working fine! ✅", 17, 47)
```

## 🚨 Important Notes
- ⚠️ Make sure WhatsApp Web is open and logged in before running the script.
- ⏳ The script will wait until the scheduled time to send the message. Ensure you leave the browser open.
- 🕑 The time given in the script should be at least 1-2 minutes in the future, so the script has enough time to open WhatsApp Web.

## 💡 License
This script is open-source and free to use. However, please respect privacy and get consent before sending automated messages. 📜

## 🤝 Contributing
Feel free to fork the repository, make changes, and create pull requests. I welcome any suggestions, improvements, or bug fixes! 🚀

---

Enjoy automating your WhatsApp messages! 😄
```
