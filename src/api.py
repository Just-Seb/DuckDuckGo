from flask import Flask, jsonify, request,send_file
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class get_cropped_image(Resource):
    def get(self):
        return {"data" : "Hello World"}

api.add_resource(get_cropped_image, "/getImage")


if __name__ == "__main__":
    app.run(debug=True)


