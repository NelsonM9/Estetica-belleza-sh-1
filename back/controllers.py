from flask import request, jsonify
from db.model import Client
from marshmallow import validate
from flask.views import MethodView
from helpers.data_manager import DataManager
from helpers.encrypt_pass import EncryptPass
from validators.client import ClientRegistration

data_m = DataManager()
encrypt = EncryptPass()
client_schema = ClientRegistration()

class Signin(MethodView):

    def post(self):
        try:
            client_signin = request.get_json()
            errors = client_schema.validate(client_signin)
            if errors:
                print(errors)
                return jsonify({'state':'error','error':errors})
            new_client = Client(
                name_c = client_signin['name'],
                lastname_c = client_signin['last_Name'],
                email = client_signin['email'],
                password = client_signin['password'],
                favorite_one = client_signin['favorite_one'],
                favorite_two = client_signin['favorite_two'],
                favorite_three = client_signin['favorite_three']
            )
            state = data_m.add(new_client)
            return jsonify({'state':state})
        except:
            return jsonify({'state':'error'})
