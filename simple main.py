from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def new():
    return render_template('index.html')

@app.route('/<string:website>')
def html_page(website):
    return render_template(website)

@app.route('/submit_form',methods=['POST','GET'])
def submit():
    return 'Form successfully submitted.Thank You '
