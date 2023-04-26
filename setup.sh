#!/usr/bin/bash
set -e

python3.10 -m venv .env
source ./.env/bin/activate
python -m pip install -r requirements.txt
python -m pip uninstall opencv-python-headless -y
python -m pip install opencv-python

echo "All done!"
