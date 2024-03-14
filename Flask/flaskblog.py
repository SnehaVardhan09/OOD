from flask import Flask #flask --app flaskblog run

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return "<h1>Hello, World!</h1>"  

@app.route("/about")
def about():
    return "<h1>About Page</h1>"  

#if __name__ == '__main__':

