from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode
import random


app = Flask(__name__)
qrcode = QRcode(app)


@app.route("/")
def index():
    qrnum = random.randint(100,900)
    return render_template("home.html",variable=qrcode(f'qr num is {qrnum}'))

@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")
