from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/mydb'
db = SQLAlchemy(app)

# Define model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

db.create_all()

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        # Extract user information from POST request
        name = request.form['name']
        email = request.form['email']

        # Insert user information into MySQL database
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return 'User added'

    if request.method == 'GET':
        # Retrieve all user information from MySQL database
        users = User.query.all()
        return str(users)

if __name__ == '__main__':
    app.run()