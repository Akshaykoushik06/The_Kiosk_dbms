import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash


def connectdb():
    conn = sqlite3.connect('test.db', check_same_thread=False)
    c = conn.cursor()
    return conn,c


# conn = sqlite3.connect('test.db', check_same_thread=False)
# c = conn.cursor()
#
# c.execute("""create table teachers(
#              t_id text primary key,
#              name text,
#              dob text,
#              doj text,
#              email text,
#              ph_no text,
#              password text)""")
#
# conn.commit()
#conn.close()


#______________________________________________ADD STUDENT OR TEACHER__________________________________________________________________

def add_student(form):
    conn,cur=connectdb()

    hashed_pass=generate_password_hash(form.password.data)
    cur.execute("insert into students values(?,?,?,?,?,?,?,?)",
                (form.usn.data,form.name.data,form.dob.data,form.yr.data,form.br.data,form.mail.data,form.ph.data,hashed_pass))

    conn.commit()
    conn.close()

def add_teacher(form):
    conn, cur = connectdb()

    hashed_pass = generate_password_hash(form.password.data)
    cur.execute("insert into teachers values(?,?,?,?,?,?,?)",
                (form.t_id.data,form.name.data,form.dob.data,form.doj.data,form.mail.data,form.ph.data,hashed_pass))

    conn.commit()
    conn.close()

#_____________________________________________FIND TEACHER OR STUDENT________________________________________________________

def find_student(form):
    conn,cur=connectdb()

    cur.execute("select password from students where usn = ?",[form.usn.data])
    stored_pass = cur.fetchone()
    entered_pass = form.password.data

    if stored_pass != None:             #user is present
        if check_password_hash(stored_pass[0],entered_pass):
            cur.execute("select usn,name from students where usn = ?",[form.usn.data])
            info = cur.fetchone()
            conn.commit()
            conn.close()
            return info,1
        else:                           #incorrect password has been entered
            info = None
            conn.commit()
            conn.close()
            return info, 0
    else:                               #user isn't present
        info = None
        conn.commit()
        conn.close()
        return info,0

def find_teacher(form):
    conn,cur=connectdb()

    cur.execute("select password from teachers where t_id = ?", [form.usn.data])
    stored_pass = cur.fetchone()
    entered_pass = form.password.data

    if stored_pass != None:  # user is present
        if check_password_hash(stored_pass[0], entered_pass):
            cur.execute("select t_id,name from teachers where t_id = ?", [form.usn.data])
            info = cur.fetchone()
            conn.commit()
            conn.close()
            return info, 1
        else:  # incorrect password has been entered
            info = None
            conn.commit()
            conn.close()
            return info, 0
    else:  # user isn't present
        info = None
        conn.commit()
        conn.close()
        return info, 0

#_______________________________________VERIFY IF STUDENT OR TEACHER EXISTS_____________________________________________

def verify_student(form):
    conn,cur=connectdb()
    cur.execute("select usn from students where usn= ?",[form.usn.data])
    info = cur.fetchone()
    conn.commit()
    conn.close()
    if info == None:
        add_student(form)   #student doesn't exist.Add him
        return 1
    else:
        return 0            #student exists.

def verify_teacher(form):
    conn,cur=connectdb()
    cur.execute("select t_id from teachers where t_id= ?",[form.t_id.data])
    info = cur.fetchone()
    conn.commit()
    conn.close()
    if info == None:
        add_teacher(form)
        return 1
    else:
        return 0

#_______________________________________________________________________________________________________________________________
