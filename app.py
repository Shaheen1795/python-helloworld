from flask import Flask
from flask import json
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/status')
def status():
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('Inside status')
    data_set = {"result": "OK -healthy"}
    response = app.response_class(response=json.dumps(data_set), status=200, mimetype='application/json')

    return response
@app.route('/metrics')
def metrics():
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.debug('This will get logged to a file')
    data_set = {"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":20}}
    response = app.response_class(response=json.dumps(data_set), status=200, mimetype='application/json')
    return response




if __name__ == "__main__":
    app.run()
