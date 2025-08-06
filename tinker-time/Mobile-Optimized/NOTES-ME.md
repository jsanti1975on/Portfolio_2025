# Tree stdout

```bash
cyber-lab-dashboard/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
│   └── images/
│       └── qr_code.png
├── uploads/
├── cash_entries/
├── success.png
└── requirements.txt
```

> Ensure folders uploads/ and cash_entries/ exist, or they’ll be created by Flask.

## Run It

```bash
# activate your venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run app
python app.py
```
