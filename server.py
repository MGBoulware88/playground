from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", color="blue")

@app.route('/play/<int:x>')
def playMore(x):
    return render_template("index.html", color="blue", x=x)

@app.route('/play/<int:x>/<string:color>')
def playMoreColors(x,color):
    return render_template("index.html", color=color, x=x)

if __name__=="__main__":
    app.run(debug=True)
