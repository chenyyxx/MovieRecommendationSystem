from flask import Blueprint
main = Blueprint('main', __name__)
from engine import RecommendationEngine

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

@main.route("/<int:user_id>/ratings", methods = ["POST"])
def add_ratings(user_id):
    # get the ratings from the Flask POST request object
    ratings_list = request.form.keys()[0].strip().split("\n")
    ratings_list = map(lambda x: x.split(","), ratings_list)
    # create a list with the format required by the negine (user_id, movie_id, rating)
    ratings = map(lambda x: (user_id, int(x[0]), float(x[1])), ratings_list)
    # add them to the model using then engine API
    recommendation_engine.add_ratings(ratings)
 
    return json.dumps(ratings)
 
 
def create_app(spark_context, dataset_path):
    global recommendation_engine 

    recommendation_engine = RecommendationEngine(spark_context, dataset_path)    
    
    app = Flask(__name__)
    app.register_blueprint(main)
    return app 