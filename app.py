from flask import Flask
from flask import json
import logging

logging.basicConfig(level=logging.DEBUG, filename="app.log", format='%(asctime)s :: %(levelname)s :: %(message)s')

app = Flask(__name__)

@app.route('/status')
def status():
  logging.debug('/status endpoint was reached')
  return app.response_class(
    response=json.dumps({"result":"OK - healthy"}),
    status=200,
    mimetype='application/json'
  )

@app.route('/metrics')
def metrics():
  logging.debug('/metrics endpoint was reached')
  return app.response_class(
    response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
    status=200,
    mimetype='application/json'
  )

@app.route("/")
def hello():
  logging.debug('/ endpoint was reached')
  return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
