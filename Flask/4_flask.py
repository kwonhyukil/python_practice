from pickle import TRUE
from flask import Flask, request, make_response, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PATH = "upload/"
os.makedirs(UPLOAD_PATH, exist_ok=True)


@app.route("/upload", methods=["GET", "POST"])
def upload():
  file_1 = request.files.get("file_1", None)
  
  file_1.save()
  
  

@app.route("/", methods=["GET", "POST"])
def home():

  file1 = request.files.get('gsc')
  
  
  file_name = file1.filename
  
  import time
  
  file_name = time.strftime("%Y%M%D")
  
  file_name = os.path.join(UPLOAD_PATH, file_name)
  
  file1.save(file_name)
  
  # DB 저장
  
  return "Hello Flask"

@app.after_request
def post_process(response):
  # 가공
  return response

if __name__ == "__main__":
  app.run(debug=True)