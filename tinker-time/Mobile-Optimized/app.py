import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
import qrcode
import netifaces

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['CASH_DIR'] = 'cash_entries'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['CASH_DIR'], exist_ok=True)

def get_local_ip():
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface).get(netifaces.AF_INET, [])
        for link in addrs:
            ip = link.get('addr')
            if ip and not ip.startswith("127."):
                return ip
    return 'localhost'

@app.route('/')
def index():
    local_ip = get_local_ip()
    qr_url = f"http://{local_ip}:8000"
    qr_path = os.path.join('static/images/qr_code.png')
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)
    qr = qrcode.make(qr_url)
    qr.save(qr_path)
    return render_template('index.html', qr_url=qr_url)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if not f or f.filename == '':
        return "No file selected", 400
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))

@app.route('/submit_cash', methods=['POST'])
def submit_cash():
    cash = request.form.get('cash_tendered', '').strip()
    if not cash:
        return "No value submitted", 400
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"cash_{timestamp}.txt"
    with open(os.path.join(app.config['CASH_DIR'], filename), 'w') as f:
        f.write(cash)
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    print(f" Access the dashboard via: http://{get_local_ip()}:8080")
    app.run(host='0.0.0.0', port=8080, debug=True)
