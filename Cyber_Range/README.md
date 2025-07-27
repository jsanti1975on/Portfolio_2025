# Cyber Range Project Summary: HTTP File Server & Dashboard

## Project Overview:

```PlainText
This project simulates a secure file server interface within a cyber range environment. It includes an advanced HTML dashboard and a custom Python-based HTTP server, designed to accept, categorize, and safely store uploaded files while displaying live cybersecurity news via RSS.
```

## Frontend (HTML Dashboard)

**Title**: Advanced Cyber Security | Fall Dashboard

**Features**:

- Grid-style panels for various modules: RHEL, Cisco, Windows Server, CompTIA Security+, TryHackMe.
- Upload panel with file submission and a button to view uploaded files.
- TryHackMe badge and public profile embedded using iframe.
- RSS feed box that fetches and displays cybersecurity headlines from SecurityWeek.
- Hover-triggered image previews for each panel for enhanced visual feedback.

---

## 🛠️ Backend (Python HTTP Server)

**Framework**: `http.server.SimpleHTTPRequestHandler` (custom subclass)

**Functions**:

- **POST**:
  - Parses multipart form data.
  - Sanitizes file names to prevent path traversal or shell injection.
  - Detects and redirects a dummy `fake_passwd` input for security testing.
  - Moves uploaded files into categorized folders by filename pattern or extension:
    - `scripts_*.sh` ➝ `/scripts/`
    - `cyberoperations_*` ➝ `/CyberOperations/`
    - `vSphere_*` ➝ `/vSphere/`
    - Audio files (`.mp3`, `.wav`) ➝ `/Music-files/`

- **GET**:
  - Serves static content and handles:
    - `/success.png` image fetch for confirmation visuals.
    - `/fetch_rss` API for client-side RSS feed loading via `fetch`.

- **Logging**:
  - Uses Python's `logging` module to track operations, errors, and debug issues.

---

## 📂 Folder Structure Created on Upload

- `/uploads/` – Temporary file staging.
- `/scripts/` – For shell or automation scripts.
- `/CyberOperations/` – Red vs Blue operational files.
- `/vSphere/` – VMware-related configurations or exports.
- `/Music-files/` – Audio content (.mp3, .wav).

---

## 🚀 Future Enhancements

- Add authentication for upload page access.
- Integrate with a backend database for file tracking.
- Dockerize the environment for easy deployment in test ranges.
- Include virus scanning (e.g., ClamAV) for uploaded files.

---

## License

This project is intended for academic and cyber range use only. MIT License or similar can be added depending on institutional policy.

---

![West Side File Server Dashboard](images/2025-07-26-dashboard.png)

**Figure: Cyber Range - West Side File Server Dashboard**

This screenshot displays the custom HTML dashboard used in the HTTP file server project. Key components include:
- Modular panels for RHEL, Cisco, Windows Server, CompTIA Security+, and TryHackMe.
- A file upload form for transmitting files over HTTP.
- Embedded TryHackMe badge and stats.
- A dynamic cybersecurity RSS news feed with updates pulled from SecurityWeek.

The dark-themed interface with neon-green accents enhances visual clarity while reinforcing a cybersecurity-centric design.


---

**Author**: JAS Digital Tools | Class of 2025 | `jas.digital.tools`
