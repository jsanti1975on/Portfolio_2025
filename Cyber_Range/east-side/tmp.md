# Temp file for commands I ran

```bash
sudo chown -R apache:apache orchids docs assignments after-work uploads
```

```bash
sudo chmod -R 755 orchids/ docs/ assignments/ after-work/ uploads/
```

```bash
sudo chcon -R -t httpd_sys_rw_content_t orchids/ docs/ assignments/ after-work/ uploads/
```

```bash
ls -Z
```

```bash
Output (good):
httpd_sys_rw_content_t
```

```bash
Stopped
```

```bash

```

```bash

```

```bash

```

```bash

```

```bash
🔐 Fix File Upload Permissions (Red Hat SELinux)

Ensure folders are writable by your current user:

sudo chown -R $USER:$USER uploads orchids docs assignments after-work


Fix SELinux write contexts:

sudo chcon -R -t httpd_sys_rw_content_t uploads orchids docs assignments after-work


If Apache is used later, switch ownership:

sudo chown -R apache:apache ...

🧠 Upload Routing Logic
Prefix	Saved To Folder
orchid_	/orchids/
doc_	/docs/
assign_	/assignments/
after_	/after-work/
(default)	/uploads/

You may define custom rules in config.yaml:

routing_rules:
  orchid_: orchids
  doc_: docs
  assign_: assignments
  after_: after-work
```
