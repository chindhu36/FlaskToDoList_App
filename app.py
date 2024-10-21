from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the ToDo model for the database
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the task
    content = db.Column(db.String(200), nullable=False)  # Task content
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for task creation

    def __repr__(self):
        return f"<ToDo {self.id}>"  # Representation of the ToDo object


# Define the main route for the application
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':  # Check if the request is a POST request
        task_content = request.form['content']  # Get task content from the form
        new_task = ToDo(content=task_content)  # Create a new ToDo object

        try:
            db.session.add(new_task)  # Add the new task to the session
            db.session.commit()  # Commit the session to save the task to the database
            return redirect('/')  # Redirect to the main page
        except:
            return 'There is an issue while adding task'  # Handle any exceptions

    else:  # If the request is a GET request
        tasks = ToDo.query.order_by(ToDo.date_created).all()  # Query all tasks ordered by creation date
        return render_template('index.html', tasks=tasks)  # Render the main template with tasks


# Define the route to delete a task
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    task_to_delete = ToDo.query.get_or_404(id)  # Get the task to delete, or return a 404 error

    try:
        db.session.delete(task_to_delete)  # Delete the task from the session
        db.session.commit()  # Commit the session to save the changes
        return redirect('/')  # Redirect to the main page
    except:
        return 'There is an issue while deleting task'  # Handle any exceptions


# Define the route to update a task
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = ToDo.query.get_or_404(id)  # Get the task to update, or return a 404 error
    if request.method == 'POST':  # Check if the request is a POST request
        task.content = request.form.get('content')  # Update the task content

        try:
            db.session.commit()  # Commit the session to save the changes
            return redirect('/')  # Redirect to the main page
        except:
            return 'There is an issue while updating task'  # Handle any exceptions
        
    else:  # If the request is a GET request
        return render_template('update.html', task=task)  # Render the update template with the task


# Run the application
if __name__ == "__main__":
    with app.app_context():  # Create the database tables
        db.create_all()
    app.run(debug=True, host="0.0.0.0")  # Start the application in debug mode
