from flask import Flask, render_template, make_response
from database import database
from flask_wtf.csrf import CsrfProtect
import subprocess
import traceback

csrf = CsrfProtect()

def create_app(environment):
    app = Flask(__name__)
    app.config.from_pyfile("config/{}.py".format(environment))
    
    database.init(app.config["DB_PATH"])

    csrf.init_app(app)

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

	@app.route('/')
	def index():
		return render_template("index.html")

	
    return app

if __name__ == "__main__":
    create_app("dev").run(port=5000, debug=True)
