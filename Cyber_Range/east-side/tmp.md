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

```
