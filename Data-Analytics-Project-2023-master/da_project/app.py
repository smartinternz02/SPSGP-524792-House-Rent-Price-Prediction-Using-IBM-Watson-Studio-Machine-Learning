from flask import Flask, redirect,url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(r"index.html")

@app.route("/about.html")
def about():
    return render_template(r"about.html")

@app.route("/bangalore.html")
def bangalore():
    return render_template(r"bangalore.html")

@app.route("/chennai.html")
def chennai():
    return render_template(r"chennai.html")

@app.route("/contact.html")
def contact():
    return render_template(r"contact.html")

@app.route("/delhi.html")
def delhi():
    return render_template(r"delhi.html")

@app.route("/feature.html")
def feature():
    return render_template(r"feature.html")

@app.route("/hyderabad.html")
def hyderabad():
    return render_template(r"hyderabad.html")

@app.route("/kolkata.html")
def kolkata():
    return render_template(r"kolkata.html")

@app.route("/mumbai.html")
def mumbai():
    return render_template(r"mumbai.html")

@app.route("/price.html")
def price():
    return render_template(r"price.html")

@app.route("/quote.html")
def quote():
    return render_template(r"quote.html")

@app.route("/service.html")
def service():
    return render_template(r"service.html")

@app.route("/team.html")
def team():
    return render_template(r"team.html")

@app.route("/testimonial.html")
def testimonial():
    return render_template(r"testimonial.html")

@app.route("/index.html")
def index():
    return render_template(r"index.html")

if __name__ == "__main__":
    app.run(debug=False, port=8000)