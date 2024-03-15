## portfoilo-site
- 개인 포트폴리오 사이트 만들어서 서버 배포까지 목표
### venv-setting
- python3 -m venv .venv
- source .venv/bin/activate

### django-setting
- pip install django
- django-admin startproject config . # 현재 폴더에서 프로젝트 생성
- python manage.py startapp users
- python manage.py startapp portfoilo
- python manage.py startapp common

### mysql 연동
- pip install mysqlclient
- db.py 만들어서 프라이빗하게 하고 settings.py에 설정
- 모델 정의 후
- python manage.py inspectdb 

### 모델 구조
1. User

- email: str unique 
- Nicname: str
- password: str

2. portfolio
- title: str
- description: str
- image: image
- link: str
- user_id: int FK

3. common
- create_at
- update_at

### Rest API

(1) User API

login
api/v1/login
- POST: 로그인

logout
api/v1/logout
- POST: 로그아웃

signup
api/v1/signup
- POST: 회원가입

UserDetaiview
- GET: 특정 유저 조회

MyInfo
- GET: 자신 정보 조회
- PUT: 자신 정보 수정

(2) Portfoilo_post API

PortfolioList
api/v1/feeds
- POST: 새로운 포트폴리오 생성
- GET: 전체 목록 조회

PortfolioDetail
- GET: 특정 포폴 상세 조회
- PUT: 특정 포폴 정보 수정
- DELETE: 특정 포폴 삭제