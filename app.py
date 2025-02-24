"""
A basic flask app
"""

from flask import Flask

## creates a flask app
app = Flask(__name__) 

## url routing/ Flask app routing
@app.route("/") #run hello() when visits '/' homepage
def welcome():
    return "Hello User!, Welcome to my flask app."

@app.route("/about")
def about():
    return "Welcome to the about page!<br>My name is Anuvansh.<br>I created this app while learning flask."

if __name__ == "__main__":
    app.run(debug=True)
