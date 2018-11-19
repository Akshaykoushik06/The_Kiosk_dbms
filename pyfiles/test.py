from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/process',method=['POST'])
def process():
    name=request.form['name']
    usn=request.form['usn']
    return render_template('new_student.html',name=name,usn=usn)
if __name__ == '__main__':
    app.run(debug=True)