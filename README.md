# West: Cyber-Lab Dashboard

This project is a **mini cyber-range dashboard** that combines:
- A custom Python backend server
- Interactive HTML pages for awareness training
- A simple CSS theme

---

## Project Structure

```
cyber-lab-dashboard/
├── server.py        # Python backend (file uploads + RSS + static serving)
├── index.html       # Main page with underscore button quiz
├── tux-talks.html   # Tux animation + "compromised" message
└── style.css        # Shared styling
```

---

## Running the Project

### 1. Install dependencies (in WSL/Ubuntu) | This will be on my home dns sinkhole/vm network.
```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install requests feedparser
```

### 2. Start the server
```bash
cd cyber-lab-dashboard
python3 server.py
```

You should see a log line like:
```
Starting httpd on port 8000...
```

### 3. Open the dashboard
In your browser, go to:
```
http://localhost:8000/index.html
```

---

## Features

1. **Authentication Quiz**
   - On `index.html`, selecting the underscore (`_`) button redirects to the Tux Talks page.

2. **Tux Talks Page**
   - Animated ASCII Tux cycles through messages and ends with a red warning:  
     > You have just been compromised!

3. **File Uploads**
   - Files can be uploaded through the dashboard.
   - Backend sanitizes filenames and routes them into appropriate directories (`scripts/`, `Music-files/`, etc).

4. **RSS Feed**
   - `/fetch_rss` endpoint retrieves the latest 5 security news items from [SecurityWeek](https://www.securityweek.com).

5. **Awareness Traps**
   - If a suspicious filename like `passwd` is uploaded, the server returns a harmless fake entry instead of storing it.

---

## Ethical Use

This project is designed **for educational awareness** only:
- Demonstrating how dashboards and file uploads work.
- Showing how even small programs can have visible impact (e.g., redirecting to a "compromised" message).
- Should only be run in a **controlled lab environment**.

Do **not** expose this server to the public internet.

---

## Code Blocks
```index.html
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
```

### style.css
```css
body {
  background: black;
  color: #34ac44;
  font-family: sans-serif;
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
```

### style css
```css
body {
  background: black;
  color: #34ac44;
  font-family: sans-serif;
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
```

### tux-talks.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tux Talks</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Tux Talks</h1>
  <div id="ascii"></div>
  <div id="speech"></div>

  <script>
    const frames = [
`      .--.
     |o_o |
     |:_/ |
    //   \\ \\
   (|     | )
  /'\\_   _/\\`
  \\___)=(___/`,

`      .--.
     |x_x |
     |:_/ |
    //   \\ \\
   (|     | )
  /'\\_   _/\\`
  \\___)=(___/`
    ];

    const speechLines = [
      "Today we start with the Start Of Authority config.",
      "These buttons will link over to each host!",
      "A user name and password are needed!",
      "This file will be a dashboard!",
      "You have just been compromised!"
    ];

    let frameIndex = 0;
    let speechIndex = 0;

    function animateTux() {
      document.getElementById('ascii').textContent = frames[frameIndex];
      frameIndex = (frameIndex + 1) % frames.length;
    }

    function showSpeechLine() {
      const speechEl = document.getElementById('speech');
      speechEl.textContent = speechLines[speechIndex];
      if (speechIndex === speechLines.length - 1) {
        speechEl.style.color = "red";
        speechEl.style.fontWeight = "bold";
      }
      speechIndex++;
      if (speechIndex < speechLines.length) {
        setTimeout(showSpeechLine, 4000);
      }
    }

    setInterval(animateTux, 800);
    showSpeechLine();
  </script>
</body>
</html>
```





