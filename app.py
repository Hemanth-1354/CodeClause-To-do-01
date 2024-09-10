from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


todo_list = [
    {"id": 1, "title": "Learn Flask", "complete": False},
    {"id": 2, "title": "Build a To-Do App", "complete": False},
    {"id": 3, "title": "Deploy app", "complete": False}
]


@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)


@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_id = len(todo_list) + 1
        todo_list.append({"id": new_id, "title": title, "complete": False})
    return redirect(url_for('index'))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    for todo in todo_list:
        if todo["id"] == todo_id:
            todo["complete"] = not todo["complete"]
            break
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    for todo in todo_list:
        if todo["id"] == todo_id:
            todo_list.remove(todo)
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
