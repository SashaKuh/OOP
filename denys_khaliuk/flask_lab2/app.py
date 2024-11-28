from flask import Flask, render_template

app = Flask(__name__, 
    template_folder='flaskr/templates',
    static_folder='flaskr/static',
    static_url_path=''
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)