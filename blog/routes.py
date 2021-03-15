from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'

    },
    {
        'author': 'Daniel',
        'title': 'Blog post 2',
        'content': 'First post content',
        'date_posted': 'July 20, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('About.html', title=about)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'danielkotev@gmail.com' and form.password.data == '123456':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check the password and email', 'danger')
    return render_template('login.html', title='Login', form=form)
