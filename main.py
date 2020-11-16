import os
import requests
from flask import Flask, jsonify, request, url_for

from register import Application
import time

app = Flask(__name__)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/", methods=["GET", "POST"])
@Application.register("首页")
def home():
    return "Welcome to web server."


@app.route("/site-map", methods=["GET", "POST"])
@Application.register("站点地图")
def site_map():
    data = {}
    for rule in app.url_map.iter_rules():
        if has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            data[url] = Application.PLUGINS[rule.endpoint]
    return jsonify(data)


@app.route("/api/mirror", methods=["GET", "POST"])
@Application.register("参数镜像反射")
def mirror():
    data = request.json
    return jsonify(data)


@app.route("/api/answer", methods=["GET", "POST"])
@Application.register("应答")
def answer():
    res = {"method": request.method}
    res["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5079, debug=True)
