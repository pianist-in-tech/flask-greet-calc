# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    num_a = int(request.args['a'])
    num_b = int(request.args['b'])
    result = add(num_a,num_b)
    return f'<h1>The result is {result}</h1>'

@app.route('/sub')
def subtraction():
    num_a = int(request.args['a'])
    num_b = int(request.args['b'])
    result = sub(num_a,num_b)
    return f'<h1>The result is {result}</h1>'

@app.route('/mult')
def multiplying():
    num_a = int(request.args['a'])
    num_b = int(request.args['b'])
    result = mult(num_a,num_b)
    return f'<h1>The result is {result}</h1>'

@app.route('/div')
def division():
    num_a = int(request.args['a'])
    num_b = int(request.args['b'])
    result = div(num_a,num_b)
    return f'<h1>The result is {result}</h1>'