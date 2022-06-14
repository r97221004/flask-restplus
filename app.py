from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)  # , doc=False

# app.config["SWAGGER_UI_JSONEDITOR"] = True

a_language = api.model(
    "Language", {"language": fields.String("The language.")})

languages = []
python = {"language": "python", "id": 1}
languages.append(python)


@api.route("/language")
class Language(Resource):

    @api.marshal_with(a_language, envelope="the_data")
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        new_language = api.payload
        new_language["id"] = len(languages) + 1
        languages.append(new_language)
        return {"result": "Language added"}, 201