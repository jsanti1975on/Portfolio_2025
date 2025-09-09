# 🌐 East Side Server (IoT Subnet Dashboard)

A lightweight full-stack project using Python’s `http.server`, Apache reverse proxy, and a dashboard UI for IoT documentation, orchid logs, uploads, and RSS feeds.

---

## 🔧 Features

- 📤 File uploads with intelligent routing (via YAML)
- 📰 Cybersecurity RSS news from [SecurityWeek](https://www.securityweek.com/feed/)
- 🕸 Apache reverse proxy to Python backend (port 8000)
- 🖼 Interactive HTML/CSS dashboard (no frameworks)
- 📁 Supports `orchids`, `docs`, `assignments`, `after-work`

---

## 🗂 Project Structure

\`\`\`
eastside-server/
│
├── server.py                   # Python server with custom routing
├── 083025-east-side-index.html # Frontend dashboard
├── config.yaml                 # YAML-based upload routing
├── templates/
│   └── success.html            # Upload success page
├── static/
│   └── success.png             # Image shown after upload
├── images/                     # ⛔️ Needs .png files added
│   ├── orchid.png
│   ├── docs.png
│   ├── after-work.png
│   ├── assignments.png
├── orchids/                    # Routed by prefix: orchid_
├── docs/                       # Routed by prefix: doc_
├── assignments/               # Routed by prefix: assign_
├── uploads/                    # Fallback location
└── after-work/                 # Routed by prefix: after_
\`\`\`

---

## 🚀 Running the Server

Install dependencies:

\`\`\`bash
pip3 install feedparser pyyaml requests
\`\`\`

Start the server:

\`\`\`bash
python3 server.py
\`\`\`

By default, it runs on:

\`\`\`
http://localhost:8000
\`\`\`

Use your server's IP if you're accessing externally (e.g. \`http://192.168.0.23:8000\`)

---

## 🔁 Apache Reverse Proxy

Apache config file (\`/etc/httpd/conf.d/eastside.conf\`):

\`\`\`apache
<VirtualHost *:80>
    ServerName eastside.local
    DocumentRoot /var/www/eastside-server
    ProxyPreserveHost On

    <Directory /var/www/eastside-server>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ProxyPass /fetch_rss http://localhost:8000/fetch_rss
    ProxyPassReverse /fetch_rss http://localhost:8000/fetch_rss

    ProxyPass /assignments/upload http://localhost:8000/assignments/upload
    ProxyPassReverse /assignments/upload http://localhost:8000/assignments/upload

    ProxyPass /upload http://localhost:8000/upload
    ProxyPassReverse /upload http://localhost:8000/upload

    ErrorLog /var/log/httpd/eastside-error.log
    CustomLog /var/log/httpd/eastside-access.log combined
</VirtualHost>
\`\`\`

Enable and start Apache:

\`\`\`bash
sudo dnf install httpd mod_proxy mod_proxy_http -y
sudo systemctl enable --now httpd
\`\`\`

---

## 📦 Upload Permissions Fix

Make sure Python has write access to target directories:

\`\`\`bash
chmod -R 777 assignments uploads
\`\`\`

---

## 🔥 Firewall Access (for external clients)

If your VM is behind a firewall or using multiple NICs:

\`\`\`bash
sudo firewall-cmd --zone=public --add-port=8000/tcp --permanent
sudo firewall-cmd --reload
\`\`\`

---

## 📸 Create Missing Images (Optional)

You can create placeholder PNGs using ImageMagick:

\`\`\`bash
convert -size 300x200 xc:gray -gravity center -pointsize 24 \
  -draw "text 0,0 'Orchid'" images/orchid.png
\`\`\`

Repeat for:
- \`docs.png\`
- \`after-work.png\`
- \`assignments.png\`

---

## 👨‍💻 Upload Routing Logic

Uploaded files are routed based on filename prefix:

| Prefix       | Routed Folder |
|--------------|----------------|
| \`orchid_\`    | \`orchids/\`     |
| \`doc_\`       | \`docs/\`        |
| \`assign_\`    | \`assignments/\` |
| \`after_\`     | \`after-work/\`  |
| *(default)*  | \`assignments/\` |

Configured in \`config.yaml\` (or use built-in defaults).

---

## 🧠 Notes

- Browser access works within the VM or LAN (use \`http://192.168.x.x:8000\`)
- If \`curl\` fails from your workstation, firewall or NIC binding is likely the issue
- Apache acts as reverse proxy only for specific endpoints

---

## 📬 Contact

Made for IoT subnet testing and personal projects. For questions, ping [jas.digital.tools].
