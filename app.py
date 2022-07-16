from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clean.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)
class Contact(db.Model):
    name=db.Column(db.String(200),primary_key=True,nullable=False)
    email=db.Column(db.String(20),nullable=False)
    Phno=db.Column(db.String(20),nullable=False,unique=True)
    mes=db.Column(db.String(200),nullable=False)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form.get("name")
        email=request.form.get("email")
        Phno=request.form.get("Phno")
        mes=request.form.get("mes")
        entery=Contact(name=name,email=email,Phno=Phno,mes=mes)
        db.session.add(entery)
        db.session.commit()
    return render_template("contact.html")

@app.route('/post')
def post():
    return render_template("post.html")

if __name__=="__main__":
    app.run(debug=True)