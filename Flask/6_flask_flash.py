from itertools import count
from flask import Flask, flash, get_flashed_messages, redirect, request, make_response, jsonify, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "test_key"

@app.route("/", methods=["GET", "POST"])
def home():
  msg = get_flashed_messages()
  
  return jsonify(msg), 200
  
count = 1
@app.route('/myflash', methods=['GET'])
def myflash():
  global count
  
  flash(f"flash {count} th")
  count += 1
  
  return "flashed", 200


if __name__ == "__main__":
    app.run(debug=True)
