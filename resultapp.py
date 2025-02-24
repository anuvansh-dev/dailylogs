"""
Simple Result Checking Web App

This is a basic Flask web application that allows users to input their marks 
in three subjects (Maths, Chemistry, Physics) through a simple HTML form. 
Based on the input, the app calculates the total percentage of marks, and displays 
whether the user has passed or failed.

Features:
- Accepts user input for marks of three subjects
- Calculates the total and percentage of marks
- Displays result (Pass/Fail) based on the percentage: Pass if % >= 35
- An about section containing the info about the app
- Simple and clean interface with minimal functionality

Built by: Anuvansh
"""


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# route for the homepage
@app.route("/")
def welcome():
    """
    Renders the homepage of the web app.
    This is the starting point of the app from where the user can navigate to the result checking form
    """ 
    return render_template("homepage.html")

# route for the about page
@app.route("/about")
def about():
   return ("""This is a basic result checking app built using flask + python.<br>
              <br>- You will need to enter your obtained marks in maths, chemistry and physics subjects for checking your result.
              <br>- It will calculate your aggregate marks and provides you with your result status(pass/fail) and aggregate marks(%).
            <br>  
            <br>Built by: Anuvansh.
           """)

# route for the passed page(if % >= 35)
@app.route("/passed/<int:marks>")
def passed(marks):
    return f"Congratulations, You passed!<br>Total Marks: {marks}%"

# route for the failed page(if % < 35)
@app.route("/fail/<int:marks>")
def fail(marks):
   return f"You Failed! (marks < 35)<br>Total Marks: {marks}%"

# route for the result checking form page
@app.route("/result", methods=["GET", "POST"])
def form():
    """
    Renders the result form and processes the user's input to calculate the result.
    If the form is submitted, it calculates the total percentage of marks obtained and determines 
    if the user has passed or failed based on a minimum threshold of 35%.
    """
    if request.method == "GET":
            return render_template("resultform.html")
    else:
            # Extracting marks from the form input
            maths = float(request.form["maths"])
            chemistry = float(request.form["chemistry"])
            physics = float(request.form["physics"])

            # Calculating total marks and percentage
            total_marks = maths + chemistry + physics
            percentage = (total_marks/300) * 100

            result = ""

            # Determine pass/fail based on the percentage
            if percentage >= 35:
                result = "passed"
            else:
                result = "fail"
            
            # Redirect to the passsed/fail page based on if condition
            return redirect(url_for(result, marks=percentage))

    
# Run the flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)