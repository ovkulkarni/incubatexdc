from flask import Blueprint, render_template, current_app, flash, url_for, request, session, flash, redirect
from twitter_utils import analyze_tweets, get_tweets

twitter = Blueprint("twitter", __name__, template_folder="templates", url_prefix="/twitter")

@twitter.route("/results/<user>/")
def show_results(user):
	tweets = get_tweets(user)
	analysis = analyze_tweets(tweets)
	all_good = True
	if any(x in analysis.values() for x in ["bad", "warning"]):
		all_good=False
	return render_template('twitter/results.html', posts=analysis, all_good=all_good)

@twitter.route("/parse/", methods=["POST"])
def parse_url():
	url = request.form.get("twitter_url")
	if url.endswith("/"): url = url[:-1]
	username = url.split("/")[-1].split("?")[0]
	return redirect(url_for('.show_results', user=username))
		

		

