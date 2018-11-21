from flask import Flask,render_template,url_for,redirect,make_response
from datetime import datetime
from forms import *
from queries import *
import pdfkit

data = None
flag = None
h_ticket = None

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

def download_h_ticket(details,t_info):
    hallticket = render_template('hallticket.html', details=details, t_info=t_info)
    pdf = pdfkit.from_string(hallticket, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Hallticket.pdf'

    return response


@app.route('/student/hallticket')
def hallticket():

    global hallticket

    cs_1 = {1:['MA1C01','Engineering Mathematics-I',3],
            2:['PH1C01','Engineering Physics',3],
            3:['CE1C01','Engineering Mechanics',3],
            4:['ME1C01','Mechanical Engineering Sciences',3],
            5:['EE1C01','Basic Electrical Engineering',3],
            6:['CS1C02','Introduction to Engineering Design',2]}

    cs_2 = {1:['MA2C01','Engineering Mathmatics-II',3],
            2:['CH2C01','Engineering Chemistry',3],
            3:['CS2C01','C-Programming',3],
            4:['EC2C01','Electronics Fundamentals',3]}

    cs_3 = {1:['MA0407','Engineering Mathematics – III',4],
            2:['CS0404','Data Structures with C',4],
            3:['CS0448','Analog and Digital Electronics',4],
            4:['CS0409','Computer Organization and Architecture',4],
            5:['CS0406','Discrete Mathematical Structures', 4],
            6:['CS0331','Unix and Shell Programming',3],
            7:['HS0001','Constitution of India and Professional Ethics',1],
            8:['MA0201','Bridge Mathematics-I',2]}

    cs_4 = {1:['MA0410','Engineering Mathematics - IV',4],
             2:['CS0408','Analysis and Design of Algorithms',4],
             3:['CS0449','Microprocessor and Interfacing',4],
             4:['CS0405','Object Oriented Programming with C++',4],
             5:['CS0411','Formal Languages and Automata Theory',4],
             6:['CS0332','Software Engineering',3],
             7:['HS0102','Environmental Studies',1],
             8:['MA0202','Bridge Mathematics-II',2]}

    cs_5 = {1:['CS0407','Data Communication and Networking',4],
            2:['CS0413','Operating Systems',4],
            3:['CS0414','Database Management Systems',4],
            4:['CS0512','System Software',5],
            5:['CS0424','Management and Entrepreneurship',4],
            6:['CS----','Elective – I',3]}

    cs_6 = {1:['CS0418','Computer Networks',4],
            2:['CS0523','Object Oriented Modeling and Design',5],
            3:['CS0425','Compiler Design',4],
            4:['CS0450','Web Technologies and Applications',4],
            5:['CS---*','Elective – II',3],
            6:['CS--**','Elective – III',3]}

    cs_7 = {1:['CS0437','Cloud Computing',4],
            2:['CS0421','Cryptography',4],
            3:['CS0422','Parallel Processing Architecture and Algorithms',4],
            4:['CS0424','Management and Entrepreneurship',4],
            5:['CS-***','Elective - V',4],
            6:['CS****','Elective - VI',4]}

    cs_8 = {1:['CS0423','Object Oriented Modeling and Design',4],
            2:['CS***-','Elective -VII',4],
            3:['CS**--','Elective - VIII',2]}


                #-------------------------------------------------------


    ec_1 = {1: ['MA1C01', 'Engineering Mathematics-I', 3],
            2: ['PH1C01', 'Engineering Physics', 3],
            3: ['CE1C01', 'Engineering Mechanics', 3],
            4: ['ME1C01', 'Mechanical Engineering Sciences', 3],
            5: ['EE1C01', 'Basic Electrical Engineering', 3],
            6: ['CS1C02', 'Introduction to Engineering Design', 2]}

    ec_2 = {1: ['MA2C01', 'Engineering Mathmatics-II', 3],
            2: ['CH2C01', 'Engineering Chemistry', 3],
            3: ['CS2C01', 'C-Programming', 3],
            4: ['EC2C01', 'Electronics Fundamentals', 3]}

    ec_3 = {1:['MA0407','Engineering Mathematics – III',4],
            2:['EC0436','Analog Electronics Circuits',4],
            3:['EC0502','Digital Electronics Circuits',5],
            4:['EC0402','Network Analysis',4],
            5:['EC0301','Electronic Instrumentation',3],
            6:['EC0403','Computer Organization and Architecture',4],
            7:['HS0101','Constitution of India and Professional Ethics',1]}

    ec_4 = {1:['MA0410','Engineering Mathematics – IV',4],
            2:['EC0437','Linear Integrated Circuits and Applications',4],
            3:['EC0504','Microcontrollers',5],
            4:['EC0404','Signals and Systems',4],
            5:['EC0302','Electro Magnetic Field Theory',3],
            6:['EC0314','Power Electronics',3],
            7:['HS0102','Environmental Studies',1]}

    ec_5 = {1:['EC0406','Control Systems',4],
            2:['EC0510','Digital Signal Processing',5],
            3:['EC0410','Operating Systems',4],
            4:['EC0433','Microprocessors Systems',4],
            5:['EC0438','Antennas and Wave Propagation',4],
            6:['EC0439','Analog and Digital Communications',4]}

    ec_6 = {1:['EC0440','Advanced Communication & Coding Theory',4],
            2:['EC0417','Embedded Systems',4],
            3:['EC0315','Digital Switching Systems',3],
            4:['EC0508','Digital Design using Verilog HDL',5],
            5:['EC0412','Data Structures using C++',4],
            6:['EC*---','Elective-1',3]}

    ec_7 = {1:['EC0413','Wireless Communications',4],
            2:['EC0414','Communication Networks',4],
            3:['EC0509','CMOS VLSI circuits',5],
            4:['EC0431','Optical Fiber Communication',4],
            5:['EC####','Elective - 2',3]}

    ec_8 = {1:['EC0416','Engineering Management',4],
            2:['EC0417','Embedded Systems',4],
            3:['EC###-','Elective - 3',4],
            4:['EC##--','Elective - 4',4]}

                        #--------------------------------------------------------


    me_1 = {1:['MA1C01','Engineering Mathmatics -I',3],
            2:['CH2C01','Engineering Chemistry',3],
            3:['CS2C01','C-Programming',3],
            4:['EC2C01','Electronics Fundamentals',3]}

    me_2 = {1:['MA2C01','Engineering Mathematics-II',3],
            2:['PH1C01','Engineering Physics',3],
            3:['CE1C01','Engineering Mechanics',3],
            4:['ME1C01','Mechanical Engineering Sciences',3],
            5:['EE1C01','Basic Electrical Engineering',3],
            6:['CS1C02','Introduction to Engineering Design',2]}

    me_3 = {1:['MA0407','Engineering Mathematics-III',4],
            2:['ME0408','Mechanical Measurements & Metrology',4],
            3:['ME0404','Basic Thermodynamics',4],
            4:['ME0405','Mechanics of Materials',4],
            5:['ME0406','Manufacturing Technology – I',4],
            6:['HS0102','Environmental Studies',1]}

    me_4 = {1:['MA0410','Mathematics – IV',4],
            2:['ME0403','Materials Science and Metallurgy',4],
            3:['ME0409','Applied Thermodynamics',4],
            4:['ME0410','Kinematics of Machinery',4],
            5:['ME0411','Manufacturing Technology – II',4],
            6:['ME0412','Fluid Mechanics',4],
            7:['HS0101','Constitution of India & Professional Ethics',1]}

    me_5 = {1:['ME0454','Design of Machine Elements – I',4],
            2:['ME0416','Dynamics of Machinery',4],
            3:['ME0328','Mechatronics',3],
            4:['ME0455','Turbomachines',4],
            5:['ME0341','Engineering Management & Entrepreneurship',3],
            6:['ME0303','CAD/CAM',3],
            7:['ME0342','Operations Research',3]}

    me_6 = {1:['ME0456','Design of Machine Elements – II',4],
            2:['ME0422','Mechanical Vibrations',4],
            3:['ME0417','Finite Element Methods',4],
            4:['ME0424','Heat Transfer',4],
            5:['ME03XX','Elective – I',3],
            6:['ME02XX','Elective – II',2]}

    me_7 = {1:['ME0463','Operations Management',4],
            2:['ME0453','Control Engineering',4],
            3:['ME0427','Renewable Energy Technologies',4],
            4:['ME0202','Research Methodology',2],
            5:['ME03XY','Elective - III',3],
            6:['ME03YY','Elective - IV',3]}

    me_8 = {1:['ME0425','Computer Integrated Manufacturing',4],
            2:['ME0464','Fluid Power Systems',4],
            3:['ME04XX','Elective VI',4]}

                        #----------------------------------------------------------

    m = datetime.now()

    if data[0][5:7] == 'CS':

        details = {1: data[1],
                   2: data[0],
                   4: 'Computer Science and Engineering'}

        if m.month>=8 and m.month<=12:                          #Odd Sem
            if data[0][3:5] == '15':

                details[3] = 7
                t_info={}

                for i in cs_7:
                    l = []
                    for j in range(3):
                        l.append(cs_7[i][j])
                    t_info[i]=l

                response = download_h_ticket(details,t_info)
                return response


            elif data[0][3:5] == '16':
                details[3] = 5
                t_info = {}

                for i in cs_5:
                    l = []
                    for j in range(3):
                        l.append(cs_5[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '17':
                details[3] = 3
                t_info = {}

                for i in cs_3:
                    l = []
                    for j in range(3):
                        l.append(cs_3[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '18':
                details[3] = 1
                t_info = {}

                for i in cs_1:
                    l = []
                    for j in range(3):
                        l.append(cs_1[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

        if m.month >= 1 and m.month <=5:                #Even Sem
            if data[0][3:5] == '15':

                details[3] = 8
                t_info={}

                for i in cs_8:
                    l = []
                    for j in range(3):
                        l.append(cs_8[i][j])
                    t_info[i]=l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '16':
                details[3] = 6
                t_info = {}

                for i in cs_6:
                    l = []
                    for j in range(3):
                        l.append(cs_6[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '17':
                details[3] = 4
                t_info = {}

                for i in cs_4:
                    l = []
                    for j in range(3):
                        l.append(cs_4[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '18':
                details[3] = 2
                t_info = {}

                for i in cs_2:
                    l = []
                    for j in range(3):
                        l.append(cs_2[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

    elif data[0][5:7] == 'EC':

        details = {1: data[1],
                   2: data[0],
                   4: 'Electronics and Communication Engineering'}

        if m.month>=8 and m.month<=12:                          #Odd Sem
            if data[0][3:5] == '15':

                details[3] = 7
                t_info={}

                for i in ec_7:
                    l = []
                    for j in range(3):
                        l.append(ec_7[i][j])
                    t_info[i]=l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '16':
                details[3] = 5
                t_info = {}

                for i in ec_5:
                    l = []
                    for j in range(3):
                        l.append(ec_5[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '17':
                details[3] = 3
                t_info = {}

                for i in ec_3:
                    l = []
                    for j in range(3):
                        l.append(ec_3[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '18':
                details[3] = 1
                t_info = {}

                for i in ec_1:
                    l = []
                    for j in range(3):
                        l.append(ec_1[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

        if m.month >= 1 and m.month <=5:                #Even Sem
            if data[0][3:5] == '15':

                details[3] = 8
                t_info={}

                for i in ec_8:
                    l = []
                    for j in range(3):
                        l.append(ec_8[i][j])
                    t_info[i]=l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '16':
                details[3] = 6
                t_info = {}

                for i in ec_6:
                    l = []
                    for j in range(3):
                        l.append(ec_6[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response


            elif data[0][3:5] == '17':
                details[3] = 4
                t_info = {}

                for i in ec_4:
                    l = []
                    for j in range(3):
                        l.append(ec_4[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '18':
                details[3] = 2
                t_info = {}

                for i in ec_2:
                    l = []
                    for j in range(3):
                        l.append(ec_2[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

    if data[0][5:7] == 'ME':

        details = {1: data[1],
                   2: data[0],
                   4: 'Mechanical Engineering'}

        if m.month>=8 and m.month<=12:                          #Odd Sem
            if data[0][3:5] == '15':

                details[3] = 7
                t_info={}

                for i in me_7:
                    l = []
                    for j in range(3):
                        l.append(me_7[i][j])
                    t_info[i]=l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '16':
                details[3] = 5
                t_info = {}

                for i in me_5:
                    l = []
                    for j in range(3):
                        l.append(me_5[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '17':
                details[3] = 3
                t_info = {}

                for i in me_3:
                    l = []
                    for j in range(3):
                        l.append(me_3[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '18':
                details[3] = 1
                t_info = {}

                for i in me_1:
                    l = []
                    for j in range(3):
                        l.append(me_1[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

        if m.month >= 1 and m.month <=5:                #Even Sem
            if data[0][3:5] == '15':

                details[3] = 8
                t_info={}

                for i in me_8:
                    l = []
                    for j in range(3):
                        l.append(me_8[i][j])
                    t_info[i]=l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '16':
                details[3] = 6
                t_info = {}

                for i in me_6:
                    l = []
                    for j in range(3):
                        l.append(me_6[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '17':
                details[3] = 4
                t_info = {}

                for i in me_4:
                    l = []
                    for j in range(3):
                        l.append(me_4[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

            elif data[0][3:5] == '18':
                details[3] = 2
                t_info = {}

                for i in me_2:
                    l = []
                    for j in range(3):
                        l.append(me_2[i][j])
                    t_info[i] = l
                response = download_h_ticket(details, t_info)
                return response

@app.route('/teacher')
def teacher():
    global data
    return render_template('teacher.html',info = data)


if __name__=='__main__':
  app.run(debug=True)
