from flask import Blueprint
main = Blueprint('main', __name__)

import json

from flask import Flask, request
from engine import RecommendationEngine

@main.route("/<int:user_id>/ratings/top/<int:count>", methods=["GET"])
def recommendations(user_id, count):
    recommendations = recommendation_engine.get_recommendations(user_id, count)
    return json.dumps(recommendations)

@main.route('/<int:user_id>/ratings/<int:movie_id>', methods=['GET'])
def get_user_movie_rating(user_id, movie_id):
    user_movie_rating = recommendation_engine.get_user_movie_rating()
    return json.dumps(user_movie_rating)