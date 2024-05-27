from flask import Flask, render_template, request, redirect, url_for
import tasks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks.get_tasks())

@app.route('/add', methods=['POST'])
def add_task():
    description = request.form['description']
    tasks.add_task(description)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    tasks.complete_task(task_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    tasks.load_tasks()
    app.run(debug=True)
