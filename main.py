from flask import Flask, request, jsonify
import json
import validation

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/likes')
def get_likes():
    total = request.args.get('names')
    return jsonify(validation.validation_names(total))



if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)


