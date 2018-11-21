from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,Email,EqualTo,any_of,Regexp



class LoginForm(FlaskForm):
    usn = StringField('username',
                       validators=[InputRequired('User ID is required'),
                       Length(min=5,max=10,message='Enter a proper User ID')])

    password = PasswordField('password',
                              validators=[InputRequired('Please enter a password'),
                              Length(min=6,message='Password must have a minimum of 6 characters')])

    submit = SubmitField('Login')




class StudentSignupForm(FlaskForm):
    name = StringField('name',
                        validators=[InputRequired()])

    usn = StringField('usn',
                       validators=[InputRequired(),
                       Length(min=10,max=10,message='Enter a proper USN')])

    yr = StringField('yr',
                      validators=[InputRequired(),
                      any_of(['1','2','3','4'],message='Enter a number between 1 and 4')])

    br = StringField('br',
                      validators=[InputRequired(),
                      any_of(['CS','EC','Mech'],message='Enter one of CS, EC ,Mech')])

    dob = StringField('dob',
                       render_kw={"placeholder": "YYYY-MM-DD"},
                       validators=[InputRequired(),
                       Regexp('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',
                                message='Enter the date in YYYY-MM-DD format')])

    mail = StringField('email',
                        validators=[InputRequired(),
                        Email(message='Enter a valid Email ID')])

    ph = StringField('ph',
                      validators=[InputRequired(),
                                  Length(min=10,max=10,message='Enter valid Phone Number')])

    password = PasswordField('password',
                              validators=[InputRequired('This field is required'),
                                          EqualTo('rpassword',message='Passwords must match'),
                                          Length(min=6,message='Password must have a minimum of 6 characters')])

    rpassword = PasswordField('rpassword',
                               validators=[InputRequired('This field is required'),
                                           Length(min=6,message='Password must have a minimum of 6 characters')])



class TeacherSignupForm(FlaskForm):
    name = StringField('name',
                        validators=[InputRequired()])

    t_id = StringField('id',
                       validators=[InputRequired(),
                       Length(min=5,max=5,message='Enter a correct ID')])

    doj = StringField('doj',
                      render_kw={"placeholder": "YYYY-MM-DD"},
                      validators=[InputRequired(),
                                  Regexp('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',
                                         message='Enter the date in YYYY-MM-DD format')])

    dob = StringField('dob',
                       render_kw={"placeholder": "YYYY-MM-DD"},
                       validators=[InputRequired(),
                       Regexp('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$',
                                message='Enter the date in YYYY-MM-DD format')])

    mail = StringField('email',
                        validators=[InputRequired(),
                        Email(message='Enter a valid Email ID')])

    ph = StringField('ph',
                      validators=[InputRequired(),
                                  Length(min=10,max=10,message='Enter valid Phone Number')])

    password = PasswordField('password',
                              validators=[InputRequired('This field is required'),
                                          EqualTo('rpassword',message='Passwords must match'),
                                          Length(min=6,message='Password must have a minimum of 6 characters')])

    rpassword = PasswordField('rpassword',
                               validators=[InputRequired('This field is required'),
                                           Length(min=6,message='Password must have a minimum of 6 characters')])
