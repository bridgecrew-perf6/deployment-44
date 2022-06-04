from flask import Flask, render_template, request
from sympy import re


import adv


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "POST":
        TV = request.form['TV']
        Radio = request.form['Radio']
        Newspaper = request.form['Newspaper']
        adv_pred = adv.adv_prediction(TV, Radio, Newspaper)
        
         
    
    return render_template("index.html")

"""@app.route("/sub", methods = ['POST'])
def submit():
    # HTML => .py
    if request.method == "POST"
        name = request.form["username"]

    # .py => HTML
    return render_template("sub.html", n = name)"""


if __name__ == "__main__":
    app.run(debug= True)