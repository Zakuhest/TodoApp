from flask import Blueprint, render_template, redirect, request
from app.db import db
from app.models.task import Task
from datetime import datetime

task_router = Blueprint("task_router", __name__)

@task_router.route('/')
def index():
    task_list = Task.query.all()
    return render_template('index.html', tasks=task_list)

@task_router.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('text')
    if task_text == "" or task_text==None:
        return redirect('/')
    
    newtask = Task(text=task_text, createdAt=datetime.now())
    db.session.add(newtask)
    db.session.commit()
    return redirect('/')

""" @task_router.route('/fix')
def fix():
    # error_task = Task.query.filter_by(id=1).first()
    error_task = Task.query.get(1)
    error_task.createdAt = datetime.now()
    db.session.commit()
    return redirect('/') """

@task_router.route('/task')
@task_router.route('/task/')
@task_router.route('/task/<int:id>')
def task(id = None):
    if id == None:
        return redirect('/')
    task = Task.query.get(id)
    if task == None:
        return redirect('/')
    return render_template('detail.html', task=task)

@task_router.route('/done', methods=['POST'])
def done():
    task_id = request.form.get('id')
    task = Task.query.get(task_id)
    if task == None:
        return redirect('/')
        
    task.doneAt = datetime.now()
    db.session.commit()
    return redirect('/task/'+str(task_id))

@task_router.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id)
    if task == None:
        return redirect('/')
        
    task.deletedAt = datetime.now()
    db.session.commit()
    return redirect('/task/'+str(id))