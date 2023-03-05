from flask import Flask, render_template, request
import requests
from restaurant import Restaurant
from user import User
from review import Review


#Restaurant data:
restaurants = []
url_restaurants = "https://api.npoint.io/e01cdad77d12aa05cfbe"
response_restaurants = requests.get(url_restaurants)
data_restaurants = response_restaurants.json()

for restaurant in data_restaurants:
    res = Restaurant(restaurant['rest_id'], restaurant['name'], restaurant['city'], restaurant['rating_init'], restaurant['rating'])
    restaurants.append(res)


#user data
users = []
url_users = "https://api.npoint.io/1f6aa24d738b1c84f185"
response_users = requests.get(url_users)
data_users = response_users.json()

for user in data_users:
    usrr = User(user['userid'], user['language'], user['gender'], user['country'], user['region'], user['birth_year'], user['income_under'], user['family_status'], user['religion'])
    users.append(usrr)


#reviews data
reviews = []
url_reviews = "https://api.npoint.io/e8d07554381e035f2d9f"
response_reviews = requests.get(url_reviews)
data_reviews = response_reviews.json()

for review in data_reviews:
    rvw = Review(review['review_id'], review['restaurant_id'], review['user_id'], review['is_better_than_expected'])
    reviews.append(rvw)


app = Flask(__name__)

#restaurant routes
@app.route('/')
def get_all_restaurants():
    return render_template("index.html", all_restaurants=restaurants)


@app.route('/restaurants/<string:rest_id>')
def get_restaurant(rest_id):
    requested_rest = None
    for rest in restaurants:
        if rest.rest_id == rest_id:
            requested_rest = rest
    return render_template("restaurant.html", restaurant=requested_rest)

#user routes
@app.route('/users')
def get_all_users():
    return render_template("users.html", all_users=users)


@app.route('/users/<string:userid>')
def get_user(userid):
    requested_usr = None
    for usr in users:
        if usr.userid == userid:
            requested_usr = usr
    return render_template("user.html", user=requested_usr)

#review routes
@app.route('/reviews')
def get_all_reviews():
    return render_template("reviews.html", all_reviews=reviews)


@app.route('/reviews/<string:review_id>')
def get_review(review_id):
    requested_review = None
    review_rest = None
    for rviw in reviews:
        if rviw.review_id == review_id:
            requested_review = rviw
            for rest in restaurants:
                if rest.rest_id == rviw.restaurant_id:
                    review_rest = rest

    return render_template("review.html", review=requested_review, restaurant=review_rest.name)

#admin forms
@app.route('/admin')
def admin_page():
    return render_template("new_user.html")

@app.route("/user_added", methods=['POST', 'GET'])
def receive_new_user():
    username = request.form['username']
    language = request.form['language']
    gender = request.form['gender']
    country = request.form['country']
    region = request.form['region']
    birth_year = request.form['birth_year']
    income_under = request.form['income_under']
    family_status = request.form['family_status']
    religion =request.form['religion']
    return f"<h1>Added New User: {username}, Language: {language}, Gender: {gender}, Country: {country}, Region: {region}, Birth Year: {birth_year}, Income Under: {income_under}, Family Status: {family_status}, Religion: {religion}</h1>"



if __name__ == '__main__':
    app.run(debug=True)

