### Flask app routing

from flask import Flask,render_template,request,redirect,url_for,jsonify

#create a simple FLask application
app = Flask(__name__)

#default runs on http://127.0.0.1:5000
@app.route("/",methods = ["GET"])
def welcome():
    return "Welcome to Flask"

@app.route("/index",methods = ["GET"])
def index():
    return "Welcome to Index page"

#variable rule
@app.route("/sucess/<int:score>")
def sucess(score):
    return "The person has passed, and the score is:" + str(score)

#Failure
@app.route("/fail/<int:score>")
def fail(score):
    return "The person has passed, and the score is:" + str(score)


@app.route("/form",methods=["GET","POST"])
def form():
    if request.method =="GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths+science+history)/3
        res = ""
        if average_marks>=50:
            res = "sucess"
        else:
            res = "fail"

        return redirect(url_for(res,score = average_marks))
        #return render_template('form.html', score=average_marks) This returns the result in the form.html

    
@app.route("/api", methods = ["POST"])
def calculate():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val+b_val)

if __name__=="__main__":
    app.run(debug=True)
