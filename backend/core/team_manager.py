class TeamManager:

    def __init__(self):

        self.teams = {}

    def create_team(self, name):

        if name not in self.teams:

            self.teams[name] = []

    def add_member(
        self,
        team,
        member,
    ):

        self.create_team(team)

        if member not in self.teams[team]:

            self.teams[team].append(member)

    def export(self):

        return self.teams