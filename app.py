from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ToDo {self.id}>"



@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        task_content=request.form['content']
        new_task=ToDo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There is an issue while adding task'

    else:
        tasks= ToDo.query.order_by(ToDo.date_created).all()
        return render_template('index.html',tasks=tasks)



@app.route('/delete/<int:id>',methods=['POST','GET'])
def delete(id):
    task_to_delete=ToDo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There is an issue while deleting task'



@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    task=ToDo.query.get_or_404(id)
    if request.method=='POST':
        task.content=request.form.get('content')

        try:
        
            db.session.commit()
            return redirect('/')
        except:
            return 'There is an issue while updating task'
        
    else:
        return render_template('update.html',task=task)

       

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")
    