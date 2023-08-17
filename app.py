from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project1.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    complete=db.Column(db.Boolean)
@app.route('/')
def index():
    todo_list=Todo.query.all()
    print(todo_list)
    return render_template('base.html',todo_list=todo_list)
  


# @app.route("/add",methods=["POST"])
# def add():
#     title1=request.form.get("title")
#     new_todo=Todo(title=title1,complete=False)
    
#     db.session.add(new_todo)
#     db.session.commit()
#     return redirect(url_for("index"))
   
with app.app_context():
    db.create_all()
@app.route("/add",methods=["POST"])
def add():
    title=request.form.get("title")
    new_todo=Todo(title=title,complete=False)
    
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo=Todo.query.get(todo_id)
    todo.complete=not todo.complete
    

    
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    
    todo=Todo.query.get(todo_id)
    db.session.delete(todo)
    
    db.session.commit()
    return redirect(url_for("index"))
   
if __name__=="__main__":
    app.run(debug=True)
