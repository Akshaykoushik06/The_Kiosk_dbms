from flask import Flask,render_template,url_for,redirect
from forms import *
from queries import *

data = None
flag = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Uchiha Itachi'


@app.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()
    global data,flag

    if form.validate_on_submit():
        if form.usn.data[:3].lower()=='4ni':
            data,flag = find_student(form)
            if flag == 0:
                return render_template('login.html',form=form,nf='Invalid User ID or Password')  #0 => not found
            return redirect(url_for('student'))      #1 => user exists
        else:
            data,flag = find_teacher(form)
            if flag == 0:
                return render_template('login.html',form=form,nf='Invalid User ID or Password')
            return redirect(url_for('teacher'))
    if flag == 2:
        return render_template('login.html', form=form, ap='User already exists')  # 2 => already present
    elif flag == 3:
        return render_template('login.html', form=form, ln='Account created successfully')  # 3 => login now

    return render_template('login.html',form=form)


@app.route('/s_signup',methods=['GET','POST'])
def s_signup():
    form = StudentSignupForm()
    global data,flag

    if form.validate_on_submit():
        info = verify_student(form)
        if info == 0:
            flag = 2
            return redirect(url_for('login'))  #2 => already present
        else:
            flag = 3
            return redirect(url_for('login'))  #3 => login now

    return render_template('s_signup.html',form=form)

@app.route('/t_signup',methods=['GET','POST'])
def t_signup():
    form = TeacherSignupForm()
    global data,flag

    if form.validate_on_submit():
        info = verify_teacher(form)
        if info == 0:
            flag = 2
            return redirect(url_for('login'))       #2 => already present
        else:
            flag = 3
            return redirect(url_for('login'))       #3 => login now

    return render_template('t_signup.html',form=form)

@app.route('/student')
def student():
    global data
    return render_template('student.html',info = data)


@app.route('/teacher')
def teacher():
    global data
    return render_template('teacher.html',info = data)


if __name__=='__main__':
  app.run(debug=True)
