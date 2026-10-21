# cad_backend_app

apt-get update -y
apt-get install -y python3.14-venv
python3.14 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

flake8 app tests
pytest -v tests

uvicorn app.main:app --reload
