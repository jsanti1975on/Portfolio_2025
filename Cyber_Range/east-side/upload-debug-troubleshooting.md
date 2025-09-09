
# 📂 Upload Error Debugging: `Internal Server Error` on `doc_`-prefixed Files

## 🧪 Context
During testing of the file upload handler on `server.py`, files with names prefixed with `doc_` (such as `doc_AvA.doc`) triggered an `HTTP 500 Internal Server Error`.

The system correctly saved the file to `/uploads/`, but failed when attempting to move it to its designated destination (based on `config.yaml` rules or default logic).

## 🧾 Error Observed in Logs

```
ERROR - Error during file upload: [Errno 13] Permission denied: 'docs/doc_AvA.doc'
```

## 🕵️ Root Cause

The upload handler uses the following code to route files based on prefix:

```python
shutil.move(filepath, os.path.join(folder, os.path.basename(filepath)))
```

- Files prefixed with `doc_` are routed to the `docs/` directory.
- However, the `docs/` folder had **read/execute** permissions for Apache but **not write**.

**Directory listing before fix:**
```bash
drwxr-xr-x. 2 apache apache 6 Sep 8 22:16 docs
```

## ✅ Solution: Fix Directory Ownership and Permissions

Update the ownership and permissions so the Apache user running the Python script can move files into it:

```bash
sudo chown apache:apache docs
sudo chmod 755 docs
```

Or, if stricter SELinux or group policies apply:

```bash
sudo chmod 775 docs
```

## 💡 Recommendation: Add Error Logging for `shutil.move`

Update your `move_file()` method in `server.py` to include clearer logging:

```python
try:
    shutil.move(filepath, os.path.join(folder, os.path.basename(filepath)))
    logger.info(f"Moved file {filename} to {folder}/")
except Exception as e:
    logger.error(f"Failed to move file {filename} to {folder}/: {e}")
    raise
```

This will help surface permission issues directly in the console or logs during future tests.

## 🧹 Next Steps

- [ ] Apply permission fix to all target folders (`orchids/`, `docs/`, `assignments/`, etc.)
- [ ] Patch code with better error handling (see above)
- [ ] Retest uploads via web UI and CLI
- [ ] Commit and push changes to GitHub
