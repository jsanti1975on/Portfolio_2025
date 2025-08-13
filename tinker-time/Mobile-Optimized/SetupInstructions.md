# Setup Instructions – Mobile-Optimized Project (Ubuntu Fresh Install)

## 1) Update & Upgrade System
sudo apt update  
sudo apt upgrade -y  
sudo apt autoremove -y  

## 2) Install Python and Tools
sudo apt install -y python3 python3-pip python3-venv  

## 3) Create Project Folder
mkdir -p ~/apps  
cd ~/apps  

**If using ZIP:**  
unzip mobile-optimized.zip  
cd Mobile-Optimized  

**If pulling from GitHub:**  
git clone https://github.com/jsanti1975on/Portfolio_2025.git  
cd Portfolio_2025/tinker-time/Mobile-Optimized  

## 4) Create Python Virtual Environment
python3 -m venv .venv  
source .venv/bin/activate  

## 5) Install Required Modules
pip install --upgrade pip  
pip install -r requirements.txt  

## 6) Prepare Data Directory
mkdir -p data  
chmod 700 data  

## 7) Run the App (Dev Mode)
export DATA_DIR="$(pwd)/data"  
python app.py  

**Access in browser:**  
http://<your-server-ip>:5000  

## 8) Run with Gunicorn (Optional – Production)
gunicorn -w 2 -b 0.0.0.0:8000 app:app  
