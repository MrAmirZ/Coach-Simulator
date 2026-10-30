import Match as mtc

class Simulate_Match:
    def __init__(self,name_home,name_away,home,away):
        self.home = home
        self.away = away
        self.name_home = name_home
        self.name_away = name_away
        self.match = mtc.Match_Engine(name_home,name_away,home,away)
        self.events = []
        self.finished = False
    def simulate(self):
        if self.finished:
            return self.get_result()
        while True:
            event = self.match.game_engine()
            if event == "half time":
                self.match.pause = False
                self.match.minute = 46
                continue
            if event == "full time":
                self.finished = True
                break
            self.events.append({"minute": self.match.minute,"event": event})
        return self.get_result()
    def get_result(self):
        return {
            "home": self.name_home,
            "away": self.name_away,
            "home_goal": self.match.home_goal,
            "away_goal": self.match.away_goal,
            "home_shots": self.match.home_shots,
            "away_shots": self.match.away_shots,
            "home_shots_on_target":
                self.match.home_shots_on_target,
            "away_shots_on_target":
                self.match.away_shots_on_target,
            "home_possession": self.match.match_possession()[0],
            "away_possession": self.match.match_possession()[1],
            "home_yellow": self.match.home_yellow,
            "away_yellow": self.match.away_yellow,
            "home_red": self.match.home_red,
            "away_red": self.match.away_red,
            "events": self.events,
            "finished": self.finished
        }