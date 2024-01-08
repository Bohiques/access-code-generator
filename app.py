from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def generator():
    return render_template("home.html")

# Pagina de error 404
def pagina_no_encontrada(error):
    return render_template("404.html"), 404


app.register_error_handler(404, pagina_no_encontrada)