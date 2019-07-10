import json
import os
from os import path
from flask import Flask, send_from_directory, current_app
from flask import Response
from flask import request
from gplaycli import gplaycli
import config
from gevent.pywsgi import WSGIServer

token_url = "https://matlink.fr/token/email/gsfid"

gpc = gplaycli.GPlaycli()
gpc.token_enable = True
gpc.token_url = token_url
gpc.retrieve_token(force_new=True)

application = Flask(__name__)


def isset(variable):
    return variable in locals() or variable in globals()


def custom_index(array, compare_function):
    for i, v in enumerate(array):
        if v == compare_function:
            return i
    return -1


@application.route('/apks/<appname>', methods=['GET'])
def download(appname):
    uploads = os.path.join(current_app.root_path, config.UPLOAD_DIR)
    return send_from_directory(directory=uploads, filename=appname + ".apk")


@application.route("/favicon.ico", methods=['GET'])
def favicon():
    return ""


@application.route("/<appname>", methods=['GET'])
def get(appname):
    appinfo = gpc.details(appname)
    if not path.exists("./apks/" + appname + "-v." + appinfo['versionString'] + ".apk"):
        gpc.download_folder = os.path.abspath('./apks/')
        gpc.append_version = True
        gpc.download([appname], [appinfo])

    if appinfo['versionString'] == '':
        appinfo['versionString'] = "1.0.0"
    if len(appinfo['files']) > 0:
        appinfo['files'][0]['url'] = str(request.url_root) + "apks/" + appname + "-v." + appinfo['versionString']
    else:
        fileinfo = list()
        fileinfo['url'] = str(request.url_root) + "apks/" + appname + "-v." + appinfo['versionString']
        appinfo['files'] = list()
        appinfo['files'].append(fileinfo)

    resp = Response(json.dumps(appinfo))
    resp.headers["Content-Type"] = "application/json"
    return resp


if __name__ == "__main__":
    app_server = WSGIServer((config.HOST, config.PORT), application)
    app_server.serve_forever()
