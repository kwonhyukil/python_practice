from flask import Flask

# Flask 클래스의 객체 생성
# __name__ : ( 현재 실행 프로그램의 경로 정보를 인자 값으로 전달 )
app = Flask(__name__)

# Routing -> view function
@app.route("/")
def home():
  # response 가 만들어져요
  return "Hello Flask" # "Hello Flask", 200, {"X-Param" : "gsc"}

print(app.url_map)
@app.route("/notice")
def notice():
  return "공지사항 풰이지"

print(app.url_map)
if __name__ == "__main__":
  app.run(debug=True)