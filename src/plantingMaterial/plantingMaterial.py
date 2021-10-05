from dataReader.dataReader import dataReader
from flask_restful import Resource
from flask import request

class plantingMaterial(Resource):
    def __init__(self):
        pointsOfInterest = [
            [(1143,615),(1959,666), 'array', 'evidence'],
            [(1143,675),(1959,732), 'array', 'evidence'],
            [(1143,744),(1959,792), 'array', 'evidence'],
            [(1143,801),(1959,849), 'array', 'evidence'],
            [(1143,858),(1959,909), 'array', 'evidence']
        ]
        query = 'src/plantingMaterial/query.jpg'
        self.reader = dataReader(pointsOfInterest, query)

    def post(self):
        if 'image' not in request.files:
            return('No image part')
        image = request.files['image']
        d = self.reader.readData(image)
        return d, 201