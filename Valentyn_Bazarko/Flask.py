from flask import Flask, render_template 

add = Flask(__name__)

@add.rout('/')
def some_function():
    return render_template('index.html')


@add.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)