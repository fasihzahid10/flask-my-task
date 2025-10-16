from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .models import Task, db

api_bp = Blueprint("api", __name__)

@api_bp.get("/tasks")
@login_required
def list_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        "id": t.id, "title": t.title, "description": t.description,
        "done": t.done, "created_at": t.created_at.isoformat()
    } for t in tasks])

@api_bp.post("/tasks")
@login_required
def create_task():
    data = request.get_json(force=True)
    title = data.get("title", "").strip()
    description = data.get("description", "").strip()
    if not title:
        return jsonify({"error": "title required"}), 400
    t = Task(title=title, description=description, owner=current_user)
    db.session.add(t)
    db.session.commit()
    return jsonify({"id": t.id}), 201

@api_bp.post("/tasks/<int:task_id>/toggle")
@login_required
def toggle(task_id):
    t = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    t.done = not t.done
    db.session.commit()
    return jsonify({"ok": True, "done": t.done})

@api_bp.delete("/tasks/<int:task_id>")
@login_required
def delete(task_id):
    t = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(t)
    db.session.commit()
    return jsonify({"ok": True})
