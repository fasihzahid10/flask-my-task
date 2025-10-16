"""
Seed the database with a demo user and some tasks.
Usage:
  python seed.py
"""
from app import create_app, db
from app.models import User, Task

app = create_app()
with app.app_context():
    if not User.query.filter_by(email="demo@example.com").first():
        u = User(email="demo@example.com")
        u.set_password("demo1234")
        db.session.add(u)
        db.session.commit()
        for i in range(1, 6):
            db.session.add(Task(title=f"Sample Task {i}", description="Demo seed task", owner=u))
        db.session.commit()
        print("Seeded demo user demo@example.com / demo1234")
    else:
        print("Demo user already exists")
