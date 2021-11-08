from flask import Flask, render_template, request, redirect
# import flask
# from flask.helpers import url_for
# from flask.typing import URLValuePreprocessorCallable

#from flask.wrappers import Request
import marks as m


app = Flask(__name__)

# from urllib.parse import urlparse, urlunparse
# FROM_DOMAIN = "bibhas86.pythonanywhere.com"
# TO_DOMAIN = "http://edpcorp.com/Global/vikramsolar/Home"

# @app.before_request
# def redirect_to_new_domain():
#     urlparts = urlparse(request.url)
#     if urlparse.netloc == FROM_DOMAIN:
#         urlparts_list = list(urlparts)
#         urlparts_list[1] = TO_DOMAIN
#         return redirect(urlunparse(urlparts_list), code=301)





@app.route("/",  methods = ["GET","POST"])
def marks():
    mp = 5
    if request.method == "POST":
        
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(hrs)
        mp = marks_pred

    return render_template("index.html", my_marks = mp)



@app.route("/sub", methods=['GET', 'POST'])
def submit():
    name = ""
    if request.method == "POST":
        name = request.form["username" ]
    else:
        name = "Bibhas"

    #.py -> Html
    return render_template("sub.html" , val_name = name )    
                                      
@app.route("/register", methods=['GET', 'POST'])
def reg():
    return render_template("register.html", val_name = "Bibhas")


@app.route("/VS", methods=['GET', 'POST'])
def vs():
    return redirect("http://edpcorp.com/Global/vikramsolar/", code = 302)



if __name__ == "__main__":
    app.run(debug=True)





