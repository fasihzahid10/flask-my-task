from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Task

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
        return render_template("tasks.html", tasks=tasks)
    return render_template("index.html")

@main_bp.post("/task/create")
@login_required
def create_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    if not title:
        flash("Title is required.", "danger")
        return redirect(url_for("main.index"))
    t = Task(title=title, description=description, owner=current_user)
    db.session.add(t)
    db.session.commit()
    flash("Task created!", "success")
    return redirect(url_for("main.index"))

@main_bp.post("/task/<int:task_id>/toggle")
@login_required
def toggle_task(task_id):
    t = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    t.done = not t.done
    db.session.commit()
    return redirect(url_for("main.index"))

@main_bp.post("/task/<int:task_id>/delete")
@login_required
def delete_task(task_id):
    t = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(t)
    db.session.commit()
    flash("Task deleted.", "info")
    return redirect(url_for("main.index"))
