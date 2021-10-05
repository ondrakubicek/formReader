from flask_restful import Resource
from flask import request

class tryme(Resource):
    def post(self):
        if 'image' not in request.files:
            return('No image part')
        image = request.files['image']
        d = "hallo"
        return d, 201