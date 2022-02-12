from flask import Flask, jsonify, request,send_file
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class getImage(Resource):
    def get(self):
        return {"data" : "Hello World"}

api.add_resource(getImage, "/getImage")


if __name__ == "__main__":
    app.run(debug=True)


