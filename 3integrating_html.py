# Integrate HTML with Flask
# HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template, request # request helps to read the posted values

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello Baby!!'
    # return render_template('index.html')
    return render_template('forms.html')

@app.route('/success/<int:score>') # route decorator
def success(score):
    # return 'The person has passed and the marks is '+ str(score) # can also return an html page here
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)  # this result in result = res will go to result.html {{Jinja_format}}      

@app.route('/fail/<int:score>') # route decorator
def fail(score):
    return 'The person has failed and the marks is '+ str(score)

# result checker HTML Page
@app.route('/submit',methods= ['POST','GET']) # form action should have same <parameter> as of @app.route('<parameter>')
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science']) #request.form['<name>']
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    res = ''
    if total_score>=50:
        res='success' # I am writting res = success because I want to redirect to route '/success/'
    else:
        res='fail'        
    return redirect(url_for(res,score=total_score))
if __name__=='__main__':
    app.run(debug=True)