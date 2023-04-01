from to_do import app, db
from to_do.forms import AddTodo
from to_do.models import Todo
from flask import render_template, redirect, url_for

@app.route('/', methods=('GET', 'POST'))
def index():
    form = AddTodo()
    list_of_tasks = Todo.query.all()
    if form.validate_on_submit():
        task = Todo(details=form.task.data, completed=False)
        task.save_task_to_db()
        list_of_tasks = Todo.query.all()
        form.task.data = ''
        return redirect(url_for('index', list_of_tasks=list_of_tasks))
    return render_template('index.html', form=form, list_of_tasks=list_of_tasks)

@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.set_task_as_complete()
    return redirect(url_for('index'))