# 🐧 Tux Talks – Cyber Lab Dashboard | setup.sh code block at end of this file 

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

---

# Set Up 
   
 make_zip.sh — (creates files, zips them into tux-talks.zip)  
```bash
# make_zip.sh
#!/usr/bin/env bash
# Creates the Tux Talks project files and packages them into tux-talks.zip
set -e

PKG="tux-talks.zip"
TMPDIR="tux-talks-temp"

# Clean up any existing temp dir / zip
rm -rf "$TMPDIR" "$PKG"
mkdir -p "$TMPDIR"/assets

cat > "$TMPDIR/index.html" <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Home Lab Dashboard</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Welcome to my Cyber-Lab Dashboard</h1>
  <h3>[Authentication Challenge] Which button proceeds?</h3>
  <button class="option-button" onclick="checkAnswer(true)">_ (underscore)</button>
  <button class="option-button" onclick="checkAnswer(false)">JavaScript</button>
  <button class="option-button" onclick="checkAnswer(false)">CSS</button>
  <p id="result"></p>

  <script>
    function checkAnswer(isCorrect) {
      const result = document.getElementById("result");
      result.innerHTML = isCorrect
        ? "Correct! Redirecting to Tux Talks..."
        : "Incorrect. Try again!";
      if (isCorrect) {
        setTimeout(() => {
          window.location.href = "tux-talks.html";
        }, 2000);
      }
    }
  </script>
</body>
</html>
EOF

cat > "$TMPDIR/style.css" <<'EOF'
body {
  background: black;
  color: #34ac44;
  font-family: monospace, sans-serif;
  text-align: center;
  padding: 20px;
}

h1 {
  color: #0f0;
  margin-bottom: 20px;
}

.option-button {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 12px 24px;
  margin: 10px;
  border-radius: 4px;
  cursor: pointer;
  transition: 0.3s;
}

.option-button:hover {
  background: rgba(13,84,216,0.8);
  transform: scale(1.2);
}

#ascii {
  white-space: pre;
  font-size: 18px;
  margin-top: 20px;
}

#speech {
  margin-top: 20px;
  font-style: italic;
  min-height: 50px;
}
EOF

cat > "$TMPDIR/assets/tux-frames.txt" <<'EOF'
      .--.
     |o_o |
     |:_/ |
    //   \\
   (|     | )
  /'\_   _/\
  \___)=(___/
---
      .--.
     |x_x |
     |:_/ |
    //   \\
   (|     | )
  /'\_   _/\
  \___)=(___/
EOF

cat > "$TMPDIR/assets/tux-speech.txt" <<'EOF'
Today we start with the Start Of Authority config.
These buttons will link over to each host!
A user name and password are needed!
This file will be a dashboard!
⚠️ You have just been compromised!
EOF

cat > "$TMPDIR/tux-talks.html" <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tux Talks</title>
  <link rel="stylesheet" href="style.css">
  <style>
    /* Blinking cursor effect */
    .cursor {
      display: inline-block;
      width: 10px;
      animation: blink 1s steps(1) infinite;
    }
    @keyframes blink {
      50% { opacity: 0; }
    }
  </style>
</head>
<body>
  <h1>Tux Talks</h1>
  <div id="ascii"></div>
  <div id="speech"></div>

  <script>
    let frames = [];
    let speechLines = [];
    let frameIndex = 0;
    let speechIndex = 0;
    let typingSpeed = 50;   // ms per character
    let lineDelay = 2000;   // wait after finishing a line

    async function loadAssets() {
      try {
        // Load ASCII frames
        const framesRes = await fetch("assets/tux-frames.txt");
        const framesText = await framesRes.text();
        frames = framesText.split("---").map(f => f.trim());

        // Load speech lines
        const speechRes = await fetch("assets/tux-speech.txt");
        const speechText = await speechRes.text();
        speechLines = speechText.split("\n").filter(line => line.trim().length > 0);

        startAnimation();
      } catch (err) {
        document.getElementById("ascii").textContent = "⚠️ Error loading Tux assets!";
        console.error(err);
      }
    }

    function animateTux() {
      if (frames.length === 0) return;
      document.getElementById("ascii").textContent = frames[frameIndex];
      frameIndex = (frameIndex + 1) % frames.length;
    }

    function typeLine(line, callback) {
      const speechEl = document.getElementById("speech");
      speechEl.innerHTML = ""; // reset before typing

      let i = 0;
      function typeChar() {
        if (i < line.length) {
          speechEl.innerHTML = line.substring(0, i + 1) + '<span class="cursor">█</span>';
          i++;
          setTimeout(typeChar, typingSpeed);
        } else {
          // keep cursor after finishing
          speechEl.innerHTML = line + '<span class="cursor">█</span>';
          if (callback) setTimeout(callback, lineDelay);
        }
      }
      typeChar();
    }

    function showSpeechLine() {
      if (speechIndex >= speechLines.length) return;

      let line = speechLines[speechIndex];
      const speechEl = document.getElementById("speech");

      // Style the final line (red + bold)
      if (speechIndex === speechLines.length - 1) {
        speechEl.style.color = "red";
        speechEl.style.fontWeight = "bold";
      }

      typeLine(line, () => {
        speechIndex++;
        if (speechIndex < speechLines.length) {
          showSpeechLine();
        }
      });
    }

    function startAnimation() {
      setInterval(animateTux, 800); // Blink tux
      showSpeechLine();             // Start speech typing
    }

    loadAssets();
  </script>
</body>
</html>
EOF

cat > "$TMPDIR/start.sh" <<'EOF'
#!/bin/bash
# 🐧 Start script for Tux Talks

PORT=8080

echo "🚀 Starting Tux Talks on http://localhost:$PORT ..."
echo "Press CTRL+C to stop."

# Use Python's built-in HTTP server
if command -v python3 &>/dev/null; then
  python3 -m http.server $PORT
elif command -v python &>/dev/null; then
  python -m SimpleHTTPServer $PORT
else
  echo "❌ Python is not installed. Please install Python 3."
  exit 1
fi
EOF

cat > "$TMPDIR/README.md" <<'EOF'
# 🐧 Tux Talks – Cyber Lab Dashboard

Welcome to **Tux Talks**, a cyber-themed dashboard with an ASCII penguin that “talks” in terminal style.

## Quick start

1. Unzip the archive:
   ```bash
   unzip tux-talks.zip
   cd tux-talks
```

#  Start the local server:

./start.sh


### Need formatting below
```bash
Open http://localhost:8080
 in your browser.

Files

index.html — authentication challenge

tux-talks.html — Tux animation + speech typing

style.css — styling

assets/tux-frames.txt — ascii frames (separate by ---)

assets/tux-speech.txt — message lines

Bandit-style unzip tips

List zip content without extracting:

unzip -l tux-talks.zip


Extract a single file to stdout (like "over the wire" quick-inspection):

unzip -p tux-talks.zip assets/tux-speech.txt | less


Extract everything:

unzip tux-talks.zip -d tux-talks


EOF

Make the files executable where appropriate

chmod +x "$TMPDIR/start.sh"

Create the zip

(
cd "$TMPDIR"
zip -r "../$PKG" . >/dev/null
)

Clean up temp dir

rm -rf "$TMPDIR"

echo "Created $PKG"
ls -lh "$PKG"


---

### How to use `make_zip.sh`

1. Save the `make_zip.sh` script locally.
2. Make it executable:
   ```bash
   chmod +x make_zip.sh


Run it:

./make_zip.sh


After it finishes you’ll have tux-talks.zip in the same folder.

Bandit / over-the-wire style notes (short)

If you transfer the zip to a remote host (or retrieve it with scp/curl), you can inspect files on the remote box without extracting:

List files: unzip -l tux-talks.zip

Print file to stdout: unzip -p tux-talks.zip assets/tux-speech.txt

Extract: unzip tux-talks.zip -d tux-talks

These are the same kind of commands used in Bandit challenges to peek at archives without a GUI.

If you want, I can also produce a base64-encoded version of the zip here so you can download it with a single curl + base64 --decode > tux-talks.zip command — handy for copying over restricted shells. Want that too?
``




