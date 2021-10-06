import csv
from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def new():
    return render_template('index.html')

@app.route('/<string:website>')
def html_page(website):
    return render_template(website)

def database_file(data):
    database=open('database.txt','a')
    name=data['fullname']
    email=data['mail']
    subject=data['subject']
    message=data['message']
    file=database.write(f'\n {name},{email},{subject},{message}')

def database_file_csv(data):
    database2=open('database.csv','a',newline='')
    name=data['fullname']
    email=data['mail']
    subject=data['subject']
    message=data['message']
    file=csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    file.writerow([name,email,subject,message])


@app.route('/submit_form',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data=request.form.to_dict()
        database_file_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something is wrong please try again'


