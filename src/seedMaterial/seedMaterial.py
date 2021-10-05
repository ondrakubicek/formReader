from dataReader.dataReader import dataReader
from flask_restful import Resource
from flask import request

class seedMaterial(Resource):
    def __init__(self):
        pointsOfInterest = [
            [(111,206),(2328,364), 'text', 'dodavatel'],
            [(2348,206),(3676,364), 'text', 'odberatel'],
            [(111,376),(2328,432), 'text', 'id'],

            [(1348,716),(2128,772), 'array', 'evidence'],
            [(1348,782),(2128,834), 'array', 'evidence'],
            [(1348,846),(2128,900), 'array', 'evidence'],
            [(1348,910),(2128,964), 'array', 'evidence'],
            [(1348,972),(2128,1026), 'array', 'evidence'],


            [(2148,716),(2512,768), 'array', 'originId'],
            [(2148,782),(2512,834), 'array', 'originId'],
            [(2148,846),(2512,900), 'array', 'originId'],
            [(2148,910),(2512,964), 'array', 'originId'],
            [(2148,972),(2512,1026), 'array', 'originId'],
        ]
        query = 'src/seedMaterial/query.jpg'
        self.reader = dataReader(pointsOfInterest, query)
    
    def post(self):
        if 'image' not in request.files:
            return('No image part')
        image = request.files['image']
        d = self.reader.readData(image)
        return d, 201