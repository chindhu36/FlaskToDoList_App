# Flask To-Do List Application

This is a simple Flask-based web application for managing tasks in a to-do list. The app allows users to create, update, and delete tasks, storing them in a SQLite database.

## Features

- Add new tasks to the to-do list.
- View all tasks sorted by the date they were created.
- Update existing tasks.
- Delete tasks from the list.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **SQLite**: A lightweight database for local storage.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **HTML/CSS**: For front-end templating.
- **Docker**: For containerizing the application.

## Prerequisites

- Python 3.10+
- Docker (if running via container)

## Setup

### Option 1: Running Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/chindhu36/To_doListFlask_App
   cd To_doListFlask_App
2. **Create a Virtual Environment (Optional but Recommended):**
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
3. **Install Dependencies:**
    pip install -r requirements.txt
4. **Set Up the Database: Open a Python shell and run the following commands to initialize the SQLite database:**
    from app import db, app
    with app.app_context():
        db.create_all()
5. **Run the Application:**
    flask run
    http://127.0.0.1:5000/

### Option 2: Running with Docker
1. **Build and Run the Docker containers:**
    docker-compose up --build



### Project Structure

    .
    ├── app.py                  # Main application file
    ├── templates/              # HTML templates for rendering the web pages
    │   ├── index.html          # Home page
    │   ├── base.html           # Base HTML file
    │   └── update.html         # Update task page
    ├── static/                 # Static files (CSS, JS, images)
    │   └── main.css            # Basic CSS for styling
    ├── requirements.txt        # Python dependencies
    ├── Dockerfile              # Docker configuration file
    ├── docker-compose.yml      # Docker Compose configuration file
    └── README.md               # Project documentation


## API Endpoints
    GET /: View all tasks.
    POST /: Add a new task.
    POST /update/int:id: Update an existing task.
    POST /delete/int:id: Delete a task.



