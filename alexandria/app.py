# coding=utf-8

from flask import Flask
from flask import jsonify
from flask import request
import config
import models
import pprint

# Initialise Flask
app = Flask(__name__)    
app.debug = False


@app.route("/drivers", methods = ["GET"])
def api_drivers():
    data = {"drivers" : conf_file.get_drivers()}
    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route("/drivers/<driver_name>")
def api_driver(driver_name):
    data = {driver_name : conf_file.get_driver_info(driver_name)}
    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route('/bruno', methods=['POST'])
def bruno():
    coucou = "Coucou " + request.json["Server"]
    #coucou = "Coucou"
    return coucou

@app.route('/ci', methods=['POST'])
def create_ci():
    pass

@app.route("/", methods = ["GET"])
def api_root():
    global alexandria_version
    data = {
        "Service"  : "Alexandria",
        "Version" : alexandria_version
    }

    resp = jsonify(data)
    resp.status_code = 200

    resp.headers["AuthorSite"] = "http://uggla.fr"

    return resp

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


if __name__ == "__main__":
    # Vars  
    alexandria_version = "0.1"
    
    # Define a PrettyPrinter for debugging.
    pp = pprint.PrettyPrinter(indent=4)
    
    # Configuration file
    conf_file = config.AlexandriaConfiguration("alexandria.conf")

    # Model
    models = models.Model()
    
    print models.reference_items
    pp.pprint(models.EthernetInterface)  # debugging example.
    pp.pprint(models.Manager)  # debugging example.
    app.run(port=int(conf_file.get_alexandria_port()))
