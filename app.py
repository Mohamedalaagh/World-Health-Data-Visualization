
from flask import Flask,  render_template, url_for , flash , redirect 
import secrets
from forms import Registration, login as LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
secret_key = secrets.token_hex(16)  # Generates a 32-character hexadecimal string
app.config['SECRET_KEY'] = secret_key # prevent Cookies modifying and Flask-WTF's CSRF protection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonic.dp'
db = SQLAlchemy()

@app.route("/")
def home():
    return  render_template('home.html')

@app.route("/about")
def about():
    return  render_template('about.html')

@app.route("/contact")
def contact():
    return  render_template('contact.html')

@app.route("/privacy")
def privacy():
    return  render_template('privacy.html')

@app.route("/visualizations")
def visualizations():
    return  render_template('visualizations.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f"Signed up successfully for the user {form.username.data}", "custom-success")
        return redirect(url_for('home'))
    return render_template("register.html", form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == "moalaa4621@email.com"
            and form.password.data == "PASS!!word123"
        ):
            flash("You have been logged in!", "custom-success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "custom-success")
    return render_template("login.html", form=form)



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True,nullable=False)
    email = db.Column(db.String(125), unique=True,nullable=False)
    password = db.Column(db.String(125), nullable=False)


    def __repe__():
        return f"User('{User.fname}', '{User.lname}', '{User.username}', '{User.email}')"



if __name__ == "__main__":
    app.run(debug=True)