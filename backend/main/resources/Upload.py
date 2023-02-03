from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
import os
UPLOAD_FOLDER = './images'

class Upload(Resource):

    @jwt_required()
    def post(self):
        file = request.files['image']
        file.save("/home/marcos/upload/" +file.filename)
        return jsonify({'message': 'File uploaded successfully'})
