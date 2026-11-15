# cad_backend_app

apt update -y
apt install -y python3.15-venv
python3.15 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

flake8 app tests
pytest -v tests

uvicorn app.main:app --reload
