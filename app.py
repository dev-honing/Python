# app.py

from flask import Flask # Flask 모듈 import

# Flask 애플리케이션 생성
app = Flask(__name__)

# 루트 URL에 대한 핸들러
@app.route('/')
def hello():
    return 'Hello, Flask!'

# 서버 실행
if __name__ == '__main__':
    app.run()