from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests from your React frontend

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email
# from flask_bcrypt import Bcrypt

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:1qaz2wsx@localhost:5432/portfolio_db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['SECRET_KEY'] = 'your_secret_key'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# bcrypt = Bcrypt(app)

# class University(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     location = db.Column(db.String(100), nullable=False)
#     established_year = db.Column(db.Integer, nullable=False)

# class Professor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     department = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(200), nullable=False)
#     university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)

# class ProfessorForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     department = StringField('Department', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Add Professor')

# @app.route('/')
# def index():
#     universities = University.query.all()
#     professors = Professor.query.all()
#     return render_template('index.html', universities=universities, professors=professors)

# @app.route('/add_professor', methods=['GET', 'POST'])
# def add_professor():
#     form = ProfessorForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         professor = Professor(name=form.name.data, department=form.department.data, email=form.email.data, password=hashed_password, university_id=1)  # Assuming university_id=1 for simplicity
#         db.session.add(professor)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('add_professor.html', form=form)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')