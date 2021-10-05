from flask import Flask
from flask_restful import Api
from plantingMaterial.plantingMaterial import plantingMaterial
from seedMaterial.seedMaterial import seedMaterial

app = Flask(__name__)
api = Api(app)

api.add_resource(plantingMaterial, "/plantingMaterial")
api.add_resource(seedMaterial, "/seedMaterial")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
