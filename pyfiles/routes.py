from flask import Flask,render_template,url_for,redirect
from forms import *
from queries import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Uchiha Itachi'


@app.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.usn.data[:3].lower()=='4ni':
            data = find_student(form)
            # return redirect(url_for('student',data=data))
            return render_template('student.html', data=data)
        else: return redirect(url_for('teacher'))
    return render_template('login.html',form=form)


@app.route('/s_signup',methods=['GET','POST'])
def s_signup():
    form = StudentSignupForm()

    if form.validate_on_submit():
        add_student(form)
        return "Added "+form.name.data+" Successfully"

    return render_template('s_signup.html',form=form)

@app.route('/t_signup',methods=['GET','POST'])
def t_signup():
    form = TeacherSignupForm()

    if form.validate_on_submit():
        add_teacher(form)
        return "Added "+form.name.data+" Successfully"

    return render_template('t_signup.html',form=form)

@app.route('/student')
def student(data):
    return render_template('student.html',data=data)


@app.route('/teacher')
def teacher():
    return render_template('teacher.html')


if __name__=='__main__':
  app.run(debug=True)
