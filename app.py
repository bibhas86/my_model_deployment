from flask import Flask, render_template, request
#from flask.wrappers import Request
import marks as m


app = Flask(__name__)


@app.route("/",  methods = ["GET","POST"])
def marks():
    mp = 5
    if request.method == "POST":
        
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(hrs)
        mp = marks_pred

    return render_template("index.html", my_marks = mp)

# @app.route("/sub", methods = ['POST'])
# def submit():
#     if request.method == "POST":
#         name = request.form["username" ]

#     #.py -> Html
#     return render_template("sub.html" , val_name = name )    



if __name__ == "__main__":
    app.run(debug=True)




