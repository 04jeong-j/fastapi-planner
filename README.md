# 설치할 라이브러리

```bash
python -m venv.venv
.venv/Scripts/activate.ps1
pip install fastapi uvicorn beanie
```

```bash
git init
New-Item .gitignore #윈도우 .venv, __pycache__

git add README.md
git commit -m "first commit!"
git branch -M main
git remote add origin https://깃헙레포주소.git
git push -u origin main
```

```bash
root
|--src/
    |--models/
    |--routes/
    |--main.py/
|--.gitignore/
|--pyproject.toml/
|--README.md/
```

```shell
uvicorn src.main:app --reload
```

# 플래너 만들기

* `로그인` 기능
    * `이메일`, `비밀번호`
* `이벤트` 추가, 삭제, 업데이트
    * `제목`, `이미지`, `설명`, `태그`, `위치`, `날짜`