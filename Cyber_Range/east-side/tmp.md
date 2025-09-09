🧰 How to Migrate to Apache HTTP Server (httpd)
1. Install Apache
sudo dnf install httpd -y
sudo systemctl enable --now httpd

2. Layout the Project

Move your project to /var/www/eastside-server:

sudo mkdir -p /var/www/eastside-server/{uploads,orchids,docs,after-work,assignments,images}
sudo cp -r your_project/* /var/www/eastside-server/


Ensure permissions:

sudo chown -R apache:apache /var/www/eastside-server
sudo chmod -R 755 /var/www/eastside-server

3. Serve the HTML via Apache

Create a config file:

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


Then reload:

sudo systemctl reload httpd


Now static files and HTML are served.

4. Backend: File Upload + RSS using Python

Apache won't run your Python script by default. You'll want to use either:

WSGI with mod_wsgi (recommended for production)

Proxying to your Python app (simpler)

🔧 Option: Run Python Backend via mod_wsgi

Install mod_wsgi:

sudo dnf install mod_wsgi -y


Convert your server script to WSGI:
We'll need to refactor the script slightly to expose it as a WSGI app (I can help rewrite it). Then place it in:

/var/www/eastside-server/app.wsgi


Configure Apache to serve WSGI:
In eastside.conf:

WSGIScriptAlias /api /var/www/eastside-server/app.wsgi

<Directory /var/www/eastside-server>
    Require all granted
</Directory>


Your upload form would now POST to /api/upload and fetch RSS from /api/fetch_rss.

5. Alternative: Run Backend with systemd + Reverse Proxy

If you're not ready for WSGI, run the Python app separately and let Apache proxy requests to it.

Set up reverse proxy:
sudo dnf install mod_proxy_http -y


In eastside.conf:

ProxyPass "/fetch_rss" "http://localhost:8000/fetch_rss"
ProxyPass "/assignments/upload" "http://localhost:8000/assignments/upload"
ProxyPassReverse "/" "http://localhost:8000/"


Start your Python server:

python3 server.py


(Optional: daemonize it with systemd)

6. Security Hardening (Basic)

Block directory listing:

Options -Indexes


Add firewall rule:

sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload


Limit upload size:

LimitRequestBody 10485760


Consider setting SELinux booleans if needed:

sudo setsebool -P httpd_can_network_connect on
