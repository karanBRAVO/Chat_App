from flask import Flask, render_template
import socket

app = Flask(__name__)
IP = socket.gethostbyname(socket.gethostname())
PORT = 12345

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(IP, PORT, debug=True)
