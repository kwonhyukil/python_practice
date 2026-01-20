from flask import Flask, redirect, request, make_response, jsonify, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PATH = "upload/"
os.makedirs(UPLOAD_PATH, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Hello Flask"
  
  
@app.route("/foo", methods=["GET"])
def foo():
  return redirect(url_for('bar'))
          # 302 -> path for bar view function, /bar
  
  
@app.route("/bar", methods=["GET"])
def bar():
  return "welcome bar", 200


@app.route("/upload", methods=["POST"])
def upload():
    file_1 = request.files.get("file_1", None)

    # 파일이 없을 경우 처리
    if not file_1:
        return "No file uploaded", 400

    # 파일명 안전하게 처리
    filename = secure_filename(file_1.filename)

    # 실제 저장 경로 생성
    save_path = os.path.join(UPLOAD_PATH, filename)

    # 파일 저장
    file_1.save(save_path)

    return "file saved", 200
  
@app.after_request
def post_process(response):
    return response


if __name__ == "__main__":
    app.run(debug=True)
