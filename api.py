from flask import Flask, send_from_directory, request, jsonify

api = Flask(__name__)


@api.route("/", defaults={'path': ''}, methods=['GET'])
@api.route('/<path:path>', methods=['GET'])
def home(path):
    return send_from_directory("static", "hello.html")

# reza

#rrrr

# @api.route("/api/<path:path>", methods=['GET', 'POST', 'PUT', 'DELETE'])
# def catchAll(path):
#     errMsg = "{} /api/{} is not yet implemented!".format(request.method, path)
#     abort(404, errMsg)


#################
# ERROR HANDLES #
#################
@api.errorhandler(401)
def unauthorized(err):
    return jsonify({ 'error': err.description }), 401


@api.errorhandler(404)
def notFound(err):
    return jsonify({ 'error': err.description }), 404



if __name__ == "__main__":
    api.run(debug=True, threaded=True)
