#!/bin/python3
"""
"""
from flask import Flask, render_template, request, jsonify
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"

app.register_blueprint(sse, url_prefix='/stream')

@app.route('/hello')
def publish_hello():
    data = request.get_json()
    sse.publish(data, type='greeting')
    return jsonify(msg="message sent"), 200

if __name__ == "__main__":
    app.run(port=5001)
