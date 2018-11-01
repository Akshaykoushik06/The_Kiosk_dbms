from flask import Flask,render_template,url_for,redirect
from flask_wtf import FlaskForm,Form
from wtforms import StringField,PasswordField,SelectField,SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired,Length,Email
from flask_sqlalchemy import SQLAlchemy
from app import app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Uchiha Itachi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/akshay/dbms_project/flasky/pyfiles/database.db'
db = SQLAlchemy(app)

class User(db.Model):
    usn = db.Column(db.String, primary_key=True)

class LoginForm(FlaskForm):
    usn = StringField('username',validators=[InputRequired('USN is required'),Length(min=10,max=10,message='Enter a proper USN fool!!')])
    password = PasswordField('password',validators=[InputRequired('Who\'ll enter password'),Length(min=6,message='Password must be minimum of 6 characters')])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    name = StringField('name',validators=[InputRequired()])
    usn = StringField('usn',validators=[InputRequired(),Length(min=10,max=10,message='Enter a proper USN fool!!')])
    #dob = DateField('dob',validators=[InputRequired(),format('%Y-%m-%d')])
    #yr = SelectField('yr',validators=[InputRequired()],choices=[('1','1'),('2','2'),('3','3'),('4','4')])
    #br = SelectField('br',validators=[InputRequired()],choices=[('1','CS'),('2','EC'),('3','Mech')])
    mail = StringField('email',validators=[InputRequired(),Email(message='Enter a valid Email')])
    ph = StringField('ph',validators=[InputRequired(),Length(min=10,max=10,message='Enter valid Phone Number')])
    password = PasswordField('password',validators=[InputRequired('Who\'ll enter password'),Length(min=6,message='Password must be minimum of 6 characters')])
    rpassword = PasswordField('rpassword',validators=[InputRequired('Who\'ll enter password'),Length(min=6,message='Password must be minimum of 6 characters')])



@app.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.usn.data[:3].lower()=='4ni':
            return redirect(url_for('student'))
        else: return redirect(url_for('teacher'))
    return render_template('login.html',form=form)

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    sform = SignupForm()

    if sform.validate_on_submit():
        return 'Hi '+ sform.name.data +' '+ sform.password.data

    return render_template('signup.html',form=sform)

if __name__=='__main__':
  app.run(debug=True)
