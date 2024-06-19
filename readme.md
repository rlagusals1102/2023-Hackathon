# 어서와 군대는 처음이지?
이 프로젝트는 군대에 대한 설명과 군 복무중인 병사들을 위한 심리상담 추천 서비스 입니다.

## 기능
- [x] 군 정보 UI/UX 제작
- [ ] 상담사 추천 UI/UX 제작 (75%)
- [x] 사용자 등록 및 인증
- [x] Django Channels와 WebSockets를 사용한 실시간 채팅 기능
- [x] 메시지 브로커로 Redis 사용


## 설치

### 기술 스택

- Python
- Django
- Redis

### 설정

1. **리포지토리 클론**

    ```bash
    git clone https://github.com/yourusername/military_project.git
    cd military_project
    ```

2. **가상 환경 생성 및 활성화**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows는 `venv\Scripts\activate`
    ```

3. **라이브러리 설치**

    ```bash
    pip install -r requirements.txt
    ```

4. **환경 변수 설정**

    프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음 내용을 추가

    ```env
    SECRET_KEY='your-secret-key'
    ```

5. **데이터베이스 마이그레이션**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **슈퍼유저 생성**

    ```bash
    python manage.py createsuperuser
    ```

7. **Redis 서버 실행**

    ```bash
    redis-server
    ```

8. **서버 실행**

    ```bash
    daphne -p 8000 military_project.asgi:application
    ```

## 사용 방법

### 사용자 등록 및 로그인

1. `http://127.0.0.1:8000/signup`으로 이동하여 새 사용자 계정을 생성
2. 등록 후, `http://127.0.0.1:8000/login`에서 로그인

### 실시간 채팅
> 로그인 후 사용 가능합니다.
1. 로그인한 후, `http://127.0.0.1:8000/chat/<room_name>/`으로 이동하여 채팅방에 참여하세요. `<room_name>`을 원하는 방 이름으로 변경하세요.
2. 채팅을 시작하세요! 당신이 보낸 메시지는 오른쪽에, 다른 사용자가 보낸 메시지는 왼쪽에 나타납니다.
