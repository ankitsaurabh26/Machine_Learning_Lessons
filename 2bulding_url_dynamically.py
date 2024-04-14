# Building url dynamically
# Variable rules and URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hellowww !!'

@app.route('/success/<int:score>') # route decorator
def success(score):
    return 'The person has passed and the marks is '+ str(score) # can also return an html page here

@app.route('/fail/<int:score>') # route decorator
def fail(score):
    return 'The person has failed and the marks is '+ str(score)

# result checker
@app.route('/results/<int:marks>') # route decorator
def results(marks):
    result = ''
    if marks<50:
        result = 'fail'
    else:
        result = 'success'
    # return result
    return redirect(url_for(result,score=marks)) # this is like : url_for(success or fail,marks) -> redirects to app.route('/success or fail/<int:score>') -> marks = score

if __name__=='__main__':
    app.run(debug=True)