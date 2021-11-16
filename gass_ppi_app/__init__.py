from flask import Flask, render_template
import sys
import os
sys.path.append(os.path.abspath(os.getcwd()))
import gassppi

app = Flask(__name__)

@app.route("/")
def index():
    name = "Albert"
    score = gassppi.add(10,20)
    return render_template("index.html", name=name, score=score)

# PPI Search pages
@app.route("/ppi-search")
def ppi_search():
    return render_template("ppi-search.html")

@app.route("/ppi-search-results")
def ppi_search_results():
    return render_template("ppi-search-results.html")

@app.route("/mol-viewer")
def mol_viewer():
    return render_template("mol-viewer.html")

# Miscellaneous pages
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
