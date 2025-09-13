# 🐧 Tux Talks – Cyber Lab Dashboard

Welcome to **Tux Talks**, a fun cyber-themed mini-dashboard built with **HTML, CSS, and JavaScript**.  
It features a simple authentication challenge, an animated ASCII penguin (Tux 🐧), and a typing terminal-style dialogue with a blinking cursor.  

---

## 🚀 Features

- **Authentication Challenge** → Pick the right button to unlock the dashboard.
- **Animated Tux** → ASCII art penguin blinks continuously.
- **Dynamic Speech** → Tux delivers lines loaded from an external text file.
- **Typing Effect** → Lines appear character-by-character with a blinking cursor `█`.
- **Modular Assets** → ASCII frames and speech lines are stored in text files for easy editing.

---

## 📂 Directory Structure
```bash
/ (root)
│
├── index.html # Authentication challenge page
├── tux-talks.html # Tux animation + speech typing
├── style.css # Shared styling
└── assets/
├── tux-frames.txt # ASCII penguin frames
└── tux-speech.txt # Tux's speech lines
```


---

## 🛠️ Setup & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/tux-talks.git
   cd tux-talks
   ```

---

## 2. Open index.html in your browser (no server required).

> Solve the authentication challenge.
> If correct, you’ll be redirected to Tux Talks.

## 3. Watch Tux blink and “talk” in terminal style.


```bash
✏️ Customization

To edit Tux’s look:
Update ASCII frames inside assets/tux-frames.txt. Separate frames with ---.

To change Tux’s dialogue:
Edit assets/tux-speech.txt. Each line = one message.

To adjust typing speed:
In tux-talks.html, modify:

let typingSpeed = 50;  // ms per character
let lineDelay = 2000;  // ms wait after each line

📸 Demo Preview

👉 (Insert screenshots or a GIF of Tux blinking and talking here)

⚡ Future Ideas

Add interactive buttons on the dashboard.

Sync blinking speed with speech typing for realism.

Make Tux respond to user input (like a chatbot).

🐧 Credits

Created for fun as a cyber-themed lab dashboard.
ASCII art inspired by Tux the Penguin (Linux mascot).
```

   
   
   








