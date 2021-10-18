from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ppi-search")
def ppi_search():
    return render_template("ppi-search.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/acknowledgements")
def acknowledgements():
    return render_template("acknowledgements.html")

if __name__ == "__main__":
    app.run()
