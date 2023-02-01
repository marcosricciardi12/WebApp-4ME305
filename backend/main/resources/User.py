from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UserModel
from sqlalchemy import func
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import admin_required

#Recurso usuario
class User(Resource):
    
    #obtener recurso
    def get(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        return user.to_json()

    #eliminar recurso
    # @admin_required
    def delete(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return 'User deleted', 204
    
    #modificar recurso
    @jwt_required()
    def put(self, id):
        user = db.session.query(UserModel).get_or_404(id)
        data = request.get_json().items()
        token_id = get_jwt_identity()
        if token_id == user.id:
            for key,value in data:
                if str(key) == 'password':
                    hash = user.change_pass(value)
                    setattr(user,key,hash)
                else:
                    setattr(user,key,value)
            db.session.add(user)
            db.session.commit()
            return user.to_json(), 201
        else:
            return 'Not allowed, only owner or admin can modify', 403

class Users(Resource):

    def get(self):
        page = 1
        per_page = 5
        users = db.session.query(UserModel)
        keys = [
            'page',
            'per_page',
            'user',
            'order_by'
        ]
        filters = {}
        for key in keys:
            arg = request.args.get(key)
            if arg != None:
                filters.update({key: arg})

        if filters:
            #Traigo todos los items del body del insomnia
            for key, value in filters.items():
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
                if key == "user":
                    users = users.filter(UserModel.user.like("%" +  value + "%"))
    
                if key == "order_by":
                    if value == 'user[desc]':
                        users = users.order_by(UserModel.user.desc())
                    if value == 'user':
                        users = users.order_by(UserModel.user)

        #Ahora pagino, guarde la consulta parcial en users
        users = users.paginate(page = page, per_page = per_page, error_out=True, max_per_page=20) #Ahora no es una lista de lementos, es una paginacion
        return jsonify({"users":[user.to_json() for user in users.items],
                        'total': users.total, 
                        'pages': users.pages, 
                        'page': page})

    def post(self):
        user = UserModel.from_json(request.get_json())
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201