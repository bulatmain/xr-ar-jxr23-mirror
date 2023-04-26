py -3.10 -m venv .env
call .env/Scripts/activate.bat
py -m pip install -r requirements.txt
py -m pip uninstall opencv-python-headless -y
py -m pip install opencv-python

echo All done!