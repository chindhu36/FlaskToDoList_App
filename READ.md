Flask To-Do List Application

This is a simple Flask-based web application for managing tasks in a to-do list. The app allows users to create, update, and delete tasks, storing them in a SQLite database.

Features

Add new tasks to the to-do list.
View all tasks sorted by the date they were created.
Update existing tasks.
Delete tasks from the list.
Technologies Used
Flask: A micro web framework for Python.
SQLite: A lightweight database for local storage.
SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
HTML/CSS: For front-end templating.
Docker: For containerizing the application.
Prerequisites
Python 3.10+
Docker (if running via container)
Setup
Option 1: Running Locally
Clone the repository:

bash
Copy code
git clone https://github.com/chindhu36/To_doListFlask_App
cd flask-todo-app
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

Open a Python shell and run the following commands to initialize the SQLite database:

python
Copy code
from app import db, app
with app.app_context():
    db.create_all()
Run the application:

bash
Copy code
flask run
Open the app in your browser at http://127.0.0.1:5000/.

Option 2: Running with Docker
Build the Docker image:

bash
Copy code
docker build -t flask-todo-app .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 flask-todo-app
Access the app at http://localhost:5000/.

Project Structure
graphql
Copy code
.
├── app.py                 # Main application file
├── models.py              # Contains the ToDo model for the database
├── templates/             # HTML templates for rendering the web pages
│   ├── index.html         # Home page
│   └── update.html        # Update task page
├── static/                # Static files (CSS, JS, images)
│   └── style.css          # Basic CSS for styling
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration file
└── README.md              # Project documentation
API Endpoints
GET /: View all tasks.
POST /: Add a new task.
POST /update/<int:id>: Update an existing task.
POST /delete/<int:id>: Delete a task.
Screenshots

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize the text and links according to your project specifics. This provides a good starting point for your documentation!