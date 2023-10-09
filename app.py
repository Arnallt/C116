from flask import Flask, render_template

app = Flask(__name__,template_folder= 'template')

@app.route("/index")

def first_webpage():

    name = 'Orange'

    return render_template('index.html', index_variable = name)

app.run(debug=True)