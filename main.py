from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def link1():
    return render_template('index.html')

@app.route('/index.html')
def link2():
    return render_template('index.html')

@app.route('/about.html')
def link3():
    return render_template('about.html')

@app.route('/pricing.html')
def link4():
    return render_template('pricing.html')

@app.route('/contact.html')
def link5():
    return render_template('contact.html')

@app.route('/components.html')
def link6():
    return render_template('components.html')

@app.route('/download.html')
def link7():
    return render_template('download.html')

