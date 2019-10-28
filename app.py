# user object
class Tracker:
    def __init__(self, game, numPlayers):
        self.name = self
        self.gmae = game
        self.numPlayers = numPlayers
        self.rules = []
        self.record = []

        # function for adding fields to our tracker object
        def trackerDefine():
            rules.append(tracker)
            return

        def trackerAdd(user, tracker):
            user.trackers.append()
            return



example user object


    {User
        trackers = [{tracker1}, {tracker2}, {tracker3}, {tracker4}, ...]

        games = [   GAME1
                    [   game1,
                        game2,
                        game3,
                        game4,
                        ...]
                    ,
                [   GAME2
                    [   game1,
                        game2,
                        game3,
                        game4,
                        ...]
                    ]
                ,
                ]
}



class User:
    # function to take user input for user object
    def __init__(self, username, password):
        self.name = self
        self.username = username
        self.password = password
        # store tracked metrics
        self.trackers = []

    def trackerMake():
        # function to take user input for tracker object
        # pass arguments to tracker class, create tracker object
        return

    def selectTracker():
        # select current tracker
        return

    def startTracking():
        # start current tracker
        return

        # function to take tracker input for current tracker

        # object for storing tracked data

        # state machine function, takes user input and
