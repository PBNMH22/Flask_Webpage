from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

names = {"Tim":{"age" : 19, "gender" : "Male"},
        "Shim" : {"age" : 20, "gender" : "Male"}}

class HelloWorld(Resource):
    def get(self,name):
        return names[name]

api.add_resource(HelloWorld,"/HelloWorld/<string:name>")

if __name__ == "__main__" :
    app.run(debug = True)