class Review:
    def __init__(self, review_id, restaurant_id, user_id, is_better_than_expected):
        self.review_id = review_id
        self.restaurant_id = restaurant_id
        self.user_id = user_id
        self.is_better_than_expected = is_better_than_expected