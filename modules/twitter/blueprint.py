from flask import Blueprint, render_template, current_app, flash, url_for, request, session, flash, redirect
from twitter_utils import analyze_tweets, get_tweets

twitter = Blueprint("twitter", __name__, template_folder="templates", url_prefix="/twitter")

@twitter.route("/results/")
def show_results():
	tweets = get_tweets()
	analysis = analyze_tweets(tweets)
	return str(analysis)

		

		

