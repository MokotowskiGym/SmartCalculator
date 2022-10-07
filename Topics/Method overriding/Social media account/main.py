class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")


class InstagramAccount(Account):
    def __init__(self, username, n_followers , n_following):
        self.media = "Instagram"
        self.n_following = n_following
        super().__init__( self.media , username, n_followers)

# create the class here


# Create the class InstagramAccount and override the __init__() method.
# The method should take parameters username, n_followers and n_following.
# The objects of the class InstagramAccount should also have
# the attribute media with the value "Instagram".
