from flask import Flask , redirect, url_for
# WSGI application 
app= Flask(__name__)

@app.route('/')
def welcome():
    return'Mohammed Azam(Data scientist)AI/ML Engineer'

@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and the marks is  "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return"the person has failed and the marks is  "+str(score)

# result checker 
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))



if __name__=='__main__':
    app.run(debug=True )

# building URL dynamically 
## variable rules anf URL building 
