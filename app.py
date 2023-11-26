from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example7711.sqlite"

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String, nullable=False)

with app.app_context():
    db.create_all()

    db.session.add(User(username="example777"))
    db.session.commit()

    users = db.session.execute(db.select(User)).scalars()

@app.route('/')
def home():
    #print(SQLAlchemy.__version__)
    return 'Hi'

@app.route('/base')
def home1():
    todoList = User.query.all()
    return render_template("base.html",var=77,todoList=todoList)

@app.route('/insert',methods=["POST"])
def insert():
    todo = request.form.get("username")
    db.session.add(User(username=todo))
    db.session.commit()
    return redirect(url_for("home1"))
    #return render_template("base.html",username=todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = User.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home1"))

if __name__ == "__main__":
    app.run()

'''from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import sqlalchemy as db

app = Flask(__name__)



engine = db.create_engine("sqlite:///european_database.sqlite")

conn = engine.connect() 


@app.route('/')
def home():
    print(sqlalchemy.__version__)
    return 'Hi'

@app.route('/base')
def home1():
    return render_template("base.html",var=77)


if __name__ == "__main__":
    app.run()'''