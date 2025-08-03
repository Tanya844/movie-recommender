from flask import Flask, render_template, request
from movie_recommender import recommend_movies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = {}
    if request.method == "POST":
        user_id = int(request.form["user_id"])
        recommendations = recommend_movies(user_id)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
