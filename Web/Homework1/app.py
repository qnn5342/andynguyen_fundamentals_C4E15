from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about-me')
def aboutme():
    return render_template("aboutme.html")

@app.route('/school')
def school():
    return redirect('http://techkids.vn', code=302, Response=None)

if __name__ == '__main__':
    app.run(debug=True)
