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
# Note I made these individualy
sudo mkdir -p /var/www/eastside-server/{uploads,orchids,docs,after-work,assignments,images}
sudo cp -r your_project/* /var/www/eastside-server/
```

```bash
sudo chown -R apache:apache /var/www/eastside-server
sudo chmod -R 755 /var/www/eastside-server
```

```bash
sudo vi /etc/httpd/conf.d/eastside.conf
<VirtualHost *:80>
    ServerName eastside.local

    DocumentRoot /var/www/eastside-server

    <Directory /var/www/eastside-server>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog /var/log/httpd/eastside-error.log
    CustomLog /var/log/httpd/eastside-access.log combined
</VirtualHost>
```
















