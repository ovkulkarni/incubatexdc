from flask import Flask, render_template, flash, redirect, make_response, request, session
from flask_cache import Cache
from flask_wtf.csrf import CsrfProtect
from werkzeug.contrib.cache import SimpleCache
import logging
import subprocess
import traceback
import os

log_formatter = logging.Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s
Message:
%(message)s
''')

csrf = CsrfProtect()

cache = Cache(config={'CACHE_TYPE': 'simple'})

def create_app(environment):
    app = Flask(__name__)
    app.config.from_pyfile("config/{}.py".format(environment))

    from modules.facebook.blueprint import fb
    from modules.twitter.blueprint import twitter

    app.register_blueprint(fb)
    app.register_blueprint(twitter)

    csrf.init_app(app)

    cache.init_app(app)
    
    @app.context_processor
    def inject_config():
        if app.config["DISPLAY_DEBUG_INFO"]:
            version = subprocess.check_output(["git", "describe", "--always"]).decode().strip()
        else:
            version = ""
        return dict(global_config=app.config, version=version)

    @app.errorhandler(404)
    def page_not_found(exc):
        return make_response(render_template("not_found.html"), 404)

    @app.errorhandler(500)
    def internal_error(exc):
        trace = traceback.format_exc()
        return make_response(render_template("internal_error.html", trace=trace), 500)

    @csrf.error_handler
    def csrf_error(reason):
        return make_response(render_template('csrf_error.html', reason=reason), 400)

    @app.route("/")
    def home_page():
        return render_template("index.html")

    @app.route("/favicon.ico")
    def favicon():
        return app.send_static_file("icon/favicon.ico")

    return app

if __name__ == '__main__':
    create_app("dev").run(port=5000, debug=True)
