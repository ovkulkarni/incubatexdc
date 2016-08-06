from flask import Blueprint, render_template, current_app, flash, url_for, request, session, flash, redirect
from facebook_utils import get_posts, analyze_posts
from requests import get
from urllib import quote
import facebook

fb = Blueprint("fb", __name__, template_folder="templates", url_prefix="/facebook")

@fb.route("/login/")
def process_code():
	if not session.get("token", None):
		if not request.args.get("code", None):
			return redirect("https://www.facebook.com/dialog/oauth?client_id={}&redirect_uri={}&response_type=code".format(
				current_app.config["FB_APP_ID"],
				quote("http://localhost:5000/facebook/login/")))
		else:
			t = request.args.get("code", "")
			r = get("https://graph.facebook.com/oauth/access_token?client_id={}&client_secret={}&code={}&redirect_uri={}".format(
				current_app.config["FB_APP_ID"], current_app.config["FB_APP_SECRET"], t,
				quote("http://localhost:5000/facebook/login/")))
			arglist= r.text.split("&")
			args = {}
			for arg in arglist:
				args[arg.split("=")[0]] = arg.split("=")[1]
			session["token"] = args["access_token"]
			return(redirect(url_for('.process_code')))
	else:
		return redirect(url_for('.show_results', user="me"))

@fb.route("/results/<user>/")
def show_results(user):
	try:
		posts = get_posts(user)
		analysis = analyze_posts(posts)
		return str(analysis)
	except facebook.GraphAPIError:
		return redirect(url_for('.process_code'))

@fb.route("/parse/", methods=["POST"])
def parse_url():
	url = request.form.get("fb_url", "")
	if url.endswith("/"): url = url[:-1]
	username = url.split("/")[-1].split("?")[0]
	return redirect(url_for('.show_results', user=username))

		

		

