from flask import Flask, request, jsonify
from ariadne import graphql_sync, load_schema_from_path, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL
from resolvers import resolvers
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, *resolvers)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return ExplorerGraphiQL().html(None), 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
