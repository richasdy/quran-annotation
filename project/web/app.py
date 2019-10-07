from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from api import *

app = Flask(__name__)
app.config["DEBUG"] = True

api = Api(app)
api.add_resource(FindSurah, "/findSurah")
api.add_resource(Register, "/register")
api.add_resource(StorePosition, "/storePosition")
api.add_resource(Login, "/login")
api.add_resource(DumpCorpusToDB, "/dumpData")

@app.route('/')
def HelloWorld():
    return "Hello World"

@app.route('/echo')
def Echo():
    return "This is Anotasi Al-Quran Website"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)