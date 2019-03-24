import os

from flask import Flask, jsonify
import requests


app = Flask(__name__)

app.config.update(
    NAME=os.getenv('NAME'),
    VERSION=os.getenv('VERSION'),
    API=os.getenv('API'),
)


@app.route('/')
def hello():
    return 'Hello Frontend!'


@app.route('/version')
def version():
    return jsonify({
        'name': app.config['NAME'],
        'version': app.config['VERSION'],
    })


@app.route('/passthrough')
def passthrough():
    r = requests.get(requests.compat.urljoin(app.config['API'], 'version'))
    return jsonify(r.json())
