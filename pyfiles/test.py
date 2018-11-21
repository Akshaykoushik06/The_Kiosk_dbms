from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bull'

@app.route('/')
def home():
    temp = render_template('test1.html')
    return temp

if __name__=='__main__':
    app.run(debug=True)