from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users2.db'
db = SQLAlchemy()
db.init_app(app)

# Init flask_login
login_manager = LoginManager()
login_manager.init_app(app)



# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 

@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not db.session.execute(db.select(User).where(User.email == request.form['email'])).scalar():
            new_user = User(
                name=request.form['name'],
                password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8),
                email=request.form['email']
            )
            print(new_user.password)
            db.session.add(new_user)
            flash('Logged in successfully.')
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets', name=new_user.name))
        else:
            flash('Email in use')
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_to_check = db.session.execute(db.select(User).where(User.email == request.form['email'])).scalar()
        if user_to_check:
            if check_password_hash(user_to_check.password, request.form['password']):
                login_user(user_to_check)
                return redirect(url_for('secrets'))
        else:
            flash('Invalid Login')
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory='static/files', path='cheat_sheet.pdf'
    )


if __name__ == "__main__":
    app.run(debug=True)
