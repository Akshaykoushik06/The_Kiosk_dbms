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


#______________________________________________ADD STUDENT AND TEACHER__________________________________________________________________

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

#_______________________________________________________________________________________________________________________________

def find_student(form):
    conn,cur=connectdb()
    cur.execute("select * from students where usn= ?",[form.usn.data])
    info = cur.fetchone()
    conn.commit()
    conn.close()
    return info