# ML-Setup
## 가상 환경 세팅(Virtual Environment)
### 가상 환경 구성
#### venv 모듈 활용
Python 버전 3 이상부터는 virtualenv라는 외부 패키지 없이 내장된 venv 모듈로 세팅이 가능합니다.

명령: `python -m venv .venv`

.venv 라는 폴더를 생성하고 그 하위에 파일들을 저장하도록 하는 명령입니다.

다른 이름으로 생성해도 상관 없지만, 관행적으로 .venv라는 이름을 쓴다고 합니다.

#### Git ignore 세팅

버전 관리는 필요하지 않으므로, .gitignore 세팅해주면 됩니다.

명령: `echo .venv/ >> .gitignore`

### 가상 환경 활성화

VS Code의 PowerShell이 아닌, Command Prompt를 이용해 터미널을 열고 아래의 명령으로 실행합니다.

명령: `.venv\Scripts\activate.bat`

이때, 주의할 점은 `슬래시(/)`가 아닌, `역슬래시(\)`여야 한다는 것입니다.

터미널 앞쪽에 (.venv)가 추가되면, 가상 환경 활성화에 성공한 것입니다.

#### 확인

가상 환경에서 세팅된 파이썬 버전을 알아보기 위해 다음 명령을 실행합니다.

명령: `python --version`

### 가상 환경에 패키지 설치

#### 패키지 매니저(pip)

파이썬 패키지 매니저는 pip 명령을 이용해 설치합니다.(Package Installer for Python)

마찬가지로 다음 명령을 실행해 pip 버전도 확인 가능합니다.

명령: `pip --version`

nodejs를 설치하면 npm도 설치되어 사용 가능한 것처럼, Python을 설치하면 pip 매니저도 설치되는 것으로 보입니다.

#### 패키지 설치

다음 명령을 이용해, Express와 유사한 포지션의 Flask를 설치하고, 서빙해보겠습니다.

명령: `pip install flask`

### 서빙하기

#### app.py 

app.py를 작성하고, 아래와 같이 Hello, Flask! 출력을 시도합니다.


```
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
```

#### 가상 환경에서 실행

아래의 명령을 실행해 가상 환경에서 서버를 실행했습니다.

명령: `python app.py`

![스크린샷](image.png)

잘 실행되는 모습입니다.

#### 실행 종료
실행 종료 방법은 크게 두 가지입니다.

1. `deactivate` 명령 실행

2. 터미널 세션 종료


하지만, 실행을 종료해도 가상 환경에 설치된 pip 패키지들은 그대로 유지됩니다.

완전히 제거하려면 가상 환경을 삭제해야 합니다.


#### 가상 환경 삭제

디렉토리(폴더) 자체를 삭제합니다.

### 패키지 관리
#### npm
npm은 디렉토리마다 json 파일로 간단하게 config 파일을 대체하는 방식으로, 패키지 정보를 확인하고 적용하기에 매우 간편합니다.

명령: `npm init -y`를 통해서 패키지 초기화가 가능하고, 명령 한 번이면 package.json이 생성되며 사용할 준비가 끝납니다.

#### pip
Python의 패키지는 기본적으로 전역(global)에 설치되고, 패키지가 wrapping 되어 있지 않아서, '시스템'에서 의존합니다.

매번 전역에 설치되는 패키지는 꽤 불편한 경험을 줍니다.

다른 프로젝트에 좋지 않은 영향을 주는 것을 방지하기 위해서 버전 관리에도 더 신경써야 합니다.

더구나, Python은 버전 간에 호환되지 않는 문제가 있어서 더 민감한 경우가 많습니다.

그래서, npm처럼 패키지를 '격리'하는 지역 단위의 패키지 관리 필요성이 대두되었고, 해결을 위해 venv와 같은 가상 환경을 사용하게 되었습니다.


다만, node처럼 '디렉토리' 기반이 아니라, '환경' 기반입니다.

여러 개의 디렉토리에서 사용할 수 있으며, OS마다 venv 환경에 접속하는 명령이 약간씩 다릅니다.

#### freeze 명령
freeze 명령을 통해 package.json과 같이 의존성 패키지 정보를 기입하고, 손쉽게 공유할 수 있습니다.

명령: `pip freeze > requirements.txt`

해당 명령을 실행하면, requirements.txt가 생성되고, 내부에 패키지 목록들을 리스트업합니다.

```
# requirements.txt

blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.2
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
Werkzeug==3.0.1

```

### 참조
공욱재 강사님 가이드

https://www.daleseo.com/python-venv/

https://yeko90.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B8%B0%EC%B4%88-windows-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95-%EB%B0%A9%EB%B2%95-%EB%B0%B0%EC%9A%B0%EA%B8%B0
