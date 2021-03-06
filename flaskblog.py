from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)

# gotten from command line
app.config["SECRET_KEY"] = '2feb611bf2173def531e32fba30e41ae'
# import secrets, secrets.token_hex(16)

posts = [
    {
        'author': "David Obidu",
        'title': 'Blog post 1',
        'content': "First post content",
        'date_posted': "April 20, 2018"
    },
    {
        'author': "Corey Schafer",
        'title': 'Blog post 2',
        'content': "Second post content",
        'date_posted': "April 21, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "abc@em.com" and form.password.data == "123456":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
