
#!/bin/bash
apt update -y
apt install -y python3 python3-pip

cat <<EOF > /home/ubuntu/app.py
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
   return {"message": "Hello from AWS CLOUD", "host": socket.gethostname()}

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
