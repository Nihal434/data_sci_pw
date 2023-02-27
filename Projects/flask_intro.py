#hello
# to enter in virtual env enter in terminal .venv\scripts\activate and make sure you are working in flask project directory
from flask import Flask 
from flask import request
app = Flask(__name__)
@app.route('/')#it same as calling the func with the help of url
def index():
    return '<h1>hello world <h1>'

@app.route('/hello1') # to route on this write /hello1 after the url similarly we can route on any func 
def index1():
    return '<h1>hello world 1 <h1>'

@app.route('/hello2') #to route at index2 write /hello2 in url
def index2():
    return '<h1>hello world 2 <h1>'

@app.route('/input')  
def  request_input():      #to take input from url we have to write ? followed by var name which is x (x=hello) after entering the route which is /input
    data= request.args.get('x')
    return  "this is my input from url {}".format(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")