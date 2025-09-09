# 09-08-2025 | Red Hat Enterprise Linux 10 | Machine: Primary Jumpbox |

```bash
sudo subscription-manager register
```

```bash
sudo dnf install command-line-assistant
```

```bash
python3 -m venv <name of virtual environment>
```

```bash
source <name of virtual environment>/bin/activate
```

```bash
sudo dnf install httpd -y
sudo systemctl enable --now httpd
```

```bash
sudo mkdir -p /var/www/eastside-server/{uploads,orchids,docs,after-work,assignments,images}
sudo cp -r your_project/* /var/www/eastside-server/
```



