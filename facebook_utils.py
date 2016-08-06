from facebook import GraphAPI
from textutils import analyze
from flask import session
from requests import get

def get_posts(user="BillGates"):
    access_token = session.get("token", None)

    graph = GraphAPI(access_token)

    profile = graph.get_object(user)

    posts = graph.get_connections(profile['id'], 'feed')

    posts_list = []
    for post in posts['data']:
        posts_list.append(post)

    return posts_list

def analyze_posts(posts):
    analysis = {}
    for post in posts:
        if post.get("message", None):
            analysis[post["id"]] = analyze(post["message"])
        else:
            analysis[post["id"]] = "none"
    return analysis


