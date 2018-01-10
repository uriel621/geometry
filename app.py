import sys
import os
from flask import Flask, render_template, request, json
from calculations.calculate import find

app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    shape = request.form['shape']
    formula = request.form['formula']
    inputs = request.form['needed_values']

    inputs = inputs.split(',')
    inputs = [(inputs[2*i], int(inputs[2*i+1])) for i in range(len(inputs)//2)]

    pairs = {}
    for pair in inputs:
        pairs[pair[0]] = pair[1]
    result = find(shape, formula, pairs)

    return json.dumps(result)

if __name__ == '__main__':    
    app.run()
