# Directory 

```bash
east-side-server/
├── server.py                         # Your Python HTTP server
├── requirements.txt                  # Python dependencies
├── 083025-east-side-index.html      # Your alternate dashboard
├── index.html                        # Default homepage (optional, could point to above)
├── templates/
│   └── success.html                  # Upload confirmation page (used in POST response)
├── static/
│   ├── success.png                   # Image shown after upload
│   └── css/                          # (optional) stylesheets if modularized
│       └── styles.css
├── orchids/                          # Uploaded orchid files
├── docs/                             # Uploaded documentation
├── after-work/                       # After-work content
├── assignments/                      # Student assignment files
├── uploads/                          # Temporary upload staging
├── logs/                             # (optional) custom server logs
└── scripts/
    └── setup.sh                      # (optional) startup automation, service scripts
```

# Setup .sh script

```bash
#!/bin/bash

echo "Setting up East Side Server directories..."

mkdir -p orchids
mkdir -p docs
mkdir -p after-work
mkdir -p assignments
mkdir -p uploads
mkdir -p logs
mkdir -p templates
mkdir -p static/css
mkdir -p scripts

touch logs/server.log

echo "Folders created:"
echo "  orchids/ docs/ after-work/ assignments/ uploads/ logs/ templates/ static/css/ scripts/"

# Optional: copy placeholder success image. Using Capt Clip for now
if [[ -f success.png ]]; then
    mv success.png static/
    echo "Moved success.png into static/"
fi

echo "Setup complete!"
```
