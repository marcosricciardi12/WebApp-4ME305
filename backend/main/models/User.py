from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(100), nullable= False)
    password = db.Column(db.String(1024), nullable= False)

    @property
    def plain_password(self):
        raise AttributeError ("No permitido")
    
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    
    def change_pass(self, password):
        return generate_password_hash(password)

    def validate_pass(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User: {self.user} , {self.email} ,{self.email} , {self.password}'
    
    def to_json(self): 
        user_json = {
            'id': self.id,
            'user': str(self.user),
            'email': str(self.email),

        }
        return user_json
    
    
    def to_json_onlyname(self):
        user_json = {
            'user': str(self.user)
        }
        return user_json
    
    @staticmethod
    #Convert JSON to Object
    def from_json(user_json):
        id = user_json.get('id')
        user = user_json.get('user')
        email = user_json.get('email')
        password = user_json.get('password')
        return User(id = id,
                    user = user,
                    email = email,
                    plain_password = password,
                    )