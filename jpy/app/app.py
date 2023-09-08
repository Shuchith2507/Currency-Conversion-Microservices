from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class jpy(Resource):
    def get(self, cur):
        result = float(f"{1.78*cur:.2f}")
        return {'result': result}


api.add_resource(jpy, '/<float:cur>')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')
