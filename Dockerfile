From python:latest
WORKDIR /flask
ADD . /flask
run pip install -r requirements.txt
cmd ["python","main.py"]