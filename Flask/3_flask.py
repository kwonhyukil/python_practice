from flask import Flask, request, make_response, jsonify

app = Flask(
  __name__,
  static_folder="resources",
  static_url_path="/contents")

print(f"app.static_folder: {app.static_folder}")
print(f"app.static_url_path: {app.static_url_path}")

@app.route("/", methods=["GET"])
def home():
  request.args
  request.files
  request.form
  request.get_json()
  # body = "Hello Flask"
  # resp = make_response(body, 200)
  # resp.headers['test 1'] = 1
  # return resp
  
  # print(request.args.get('sort'))
  # print(request.headers.get("Content-Type"))
  # return "hello", 200, { "test-code": "GSC"}
  
  return jsonify({ "name": "나는 권혁일", "age": "나이는 26살" })

@app.after_request
def post_process(response):
  # 가공
  return response

if __name__ == "__main__":
  app.run(debug=True)