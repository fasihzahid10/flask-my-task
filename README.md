# flask-task-manager

A **production-ready, portfolio-grade Flask Task Manager** with:
- User auth (register/login/logout) via Flask-Login
- Tasks CRUD (create, mark done, delete)
- REST API (`/api/*`) for programmatic access
- SQLite by default, configurable via `DATABASE_URL`
- Tests (pytest), seed script, Dockerfile, Procfile
- Clean HTML templates and minimal CSS (no JS build step)

## ⚡ Quick Start (Local)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
python seed.py                # optional: creates demo user + sample tasks
python run.py                 # starts dev server at http://127.0.0.1:5000
```
**Demo login (if you ran seed):** `demo@example.com / demo1234`

## 🧪 Run tests
```bash
pytest -q
```

## 🐳 Docker (prod-ish)
```bash
docker build -t task-manager .
docker run -p 8000:8000 task-manager
```

## 🔌 REST API Examples
> Authenticate in browser first, then call endpoints (session cookie).

- `GET /api/tasks` → list tasks
- `POST /api/tasks` JSON: `{"title": "Buy milk", "description": "2L"}`
- `POST /api/tasks/<id>/toggle`
- `DELETE /api/tasks/<id>`

## 📁 Project Structure
```
flask-task-manager/
├─ app/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ views.py
│  ├─ auth.py
│  ├─ api.py
│  └─ templates/ (layout, index, login, register, tasks)
├─ app/static/css/style.css
├─ tests/test_app.py
├─ run.py
├─ seed.py
├─ requirements.txt
├─ Dockerfile
├─ Procfile
├─ .env.example
└─ .gitignore
```

## 💼 LinkedIn blurb (paste & edit)
> Built and shipped a Flask Task Manager with auth, CRUD, SQLite, and a small REST API. Added tests + Dockerfile for smooth deploys. Repo link in comments—feedback welcome!

**License:** MIT
