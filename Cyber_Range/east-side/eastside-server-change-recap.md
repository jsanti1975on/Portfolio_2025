
# 🔁 Recap: Upcoming Changes to `eastside-server`

---

## 🗂️ Directory Overview (Before Changes)

```
/var/www/eastside-server
├── after-work/
├── assignments/
│   └── https_server.py
├── docs/
├── images/
│   ├── after-work.png
│   ├── assignments.png
│   ├── docs.png
│   └── orchid.png
├── index.html
├── orchids/
├── server.py
├── uploads/
│   ├── doc_AvA.doc
│   └── doc_AvA.docx
```

---

## 🐛 Issues Identified

- ❌ `HTTP 500` Internal Server Error during file upload
- 🔒 Permissions error when moving files (e.g., `docs/`)
- 🔇 Logging only to console, not persistent
- ❌ Image 404s due to missing static serving logic
- 🔐 Reverse proxy in Apache not yet configured

---

## ✅ Planned Changes

### 1. 📄 Add Persistent Logging

**Drop-in Code:**
```python
file_handler = logging.FileHandler('eastside.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
```

**Log File Location:**
```bash
/var/www/eastside-server/eastside.log
```

---

### 2. 🔐 Fix Permissions

Ensure directories are writable:

```bash
sudo chown -R apache:apache /var/www/eastside-server/
sudo chmod -R 755 /var/www/eastside-server/
```

To be safe:
```bash
chmod 775 uploads/ assignments/ docs/ after-work/ orchids/
```

---

### 3. 🛠️ Upload Logic Improvements

**Enhance move function:**
```python
try:
    shutil.move(filepath, os.path.join(folder, os.path.basename(filepath)))
    logger.info(f"Moved file {filename} to {folder}/")
except Exception as e:
    logger.error(f"Failed to move file {filename} to {folder}/: {e}")
    raise
```

---

### 4. 🖼️ Image Fixes

Serve images directly if not already handled:

```python
elif self.path.startswith('/images/'):
    file_path = '.' + self.path
    if os.path.exists(file_path):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        with open(file_path, 'rb') as f:
            self.wfile.write(f.read())
        return
    else:
        self.send_error(404, 'Image not found')
        return
```

---

### 5. 🧱 (Optional) Apache Reverse Proxy (Future Step)

Will include:
- ProxyPass config
- CORS headers
- HTTPS/SSL
- SELinux/Firewall updates

---

## 📝 Summary Table

| Step | Change | Status |
|------|--------|--------|
| 1 | Persistent logging | ✅ Ready |
| 2 | Folder permissions | ✅ Ready |
| 3 | Upload file routing | ✅ Ready |
| 4 | Image handling | ✅ Ready |
| 5 | Apache reverse proxy | ⏳ Later |

---

**Next:** Push this to GitHub as part of your prep before implementing the code changes.
