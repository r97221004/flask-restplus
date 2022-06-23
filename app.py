from flask import Flask, Blueprint, request
from flask_restplus import Api, Resource, fields, reqparse

app = Flask(__name__)
blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, doc="/documentation")  # , doc=False

app.register_blueprint(blueprint)

# app.config["SWAGGER_UI_JSONEDITOR"] = True

a_language = api.model(
    "Language", {"language": fields.String("The language.")})

languages = []
python = {"language": "python", "id": 1}
languages.append(python)


@api.route("/language")
class Language(Resource):

    @api.marshal_with(a_language, envelope="the_data")
    @api.response(201, 'Success')
    @api.response(400, 'Validation Error')
    def get(self):
        return languages

    @api.expect(a_language)
    @api.response(201, "Success")
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("language", type=str,
                            required=True, help="language required")
        data = parser.parse_args()
        # print(data)
        new_language = data
        new_language["id"] = len(languages) + 1
        languages.append(new_language)
        return {"result": "Language added"}, 201


@api.route("/test")
class Test(Resource):

    def post(self):
        data = request.get_json(force=True)
        print(data)

        return {"Hello": "World"}
