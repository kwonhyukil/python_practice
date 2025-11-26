import re
from flask import Flask, request


app = Flask(__name__)

# Path : /, Method : Get

# @app.route("/", methods=["GET"])
# def home():
#   print(f"Path: {request.path}")
#   print(f"Method: {request.method}")
  
#   return "Hello Flask", 200, {"GSC": "gsc"}

# if __name__ == "__main__":
#   app.run(debug=True)
  
@app.route("/files", methods=["POST", "GET"])
def download():
  
  uploaded_file_name = None
  
  file_obj = request.files.get("files")
  if (file_obj):
    uploaded_file_name = file_obj.filename
    
  return {
    "method": request.method,
    "url": request.url,
    "path": request.path,
    "query": request.args,
    "form": request.form,
    "headers": dict(request.headers),
    "cookies": request.cookies,
    "files": uploaded_file_name,
    "json": request.get_json(silent=True),
    "remote_addr": request.remote_addr
  }
  
if __name__ == "__main__":
  app.run(debug=True)
  