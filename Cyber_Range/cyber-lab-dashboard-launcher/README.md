# Cyber-Lab Dashboard

This project is a **mini cyber-range dashboard** that combines:
- A custom Python backend server
- Interactive HTML pages for awareness training
- A simple CSS theme

---

## 📂 Project Structure

```
cyber-lab-dashboard/
├── server.py        # Python backend (file uploads + RSS + static serving)
├── index.html       # Main page with underscore button quiz
├── tux-talks.html   # Tux animation + "compromised" message
└── style.css        # Shared styling
```

---

## ▶️ Running the Project

### 1. Install dependencies (in WSL/Ubuntu)
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

## 🔹 Features

1. **Authentication Quiz**
   - On `index.html`, selecting the underscore (`_`) button redirects to the Tux Talks page.

2. **Tux Talks Page**
   - Animated ASCII Tux cycles through messages and ends with a red warning:  
     > ⚠️ You have just been compromised!

3. **File Uploads**
   - Files can be uploaded through the dashboard.
   - Backend sanitizes filenames and routes them into appropriate directories (`scripts/`, `Music-files/`, etc).

4. **RSS Feed**
   - `/fetch_rss` endpoint retrieves the latest 5 security news items from [SecurityWeek](https://www.securityweek.com).

5. **Awareness Traps**
   - If a suspicious filename like `passwd` is uploaded, the server returns a harmless fake entry instead of storing it.

---

## ⚠️ Ethical Use

This project is designed **for educational awareness** only:
- Demonstrating how dashboards and file uploads work.
- Showing how even small programs can have visible impact (e.g., redirecting to a "compromised" message).
- Should only be run in a **controlled lab environment**.

Do **not** expose this server to the public internet.

---

## 🛠 Next Steps

- Add screenshots to the `assets/` folder.
- Extend the dashboard with more awareness challenges.
- Push the repo to GitHub for portfolio use.
