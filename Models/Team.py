class Team:
    def __init__(self, team_name, group, world_rank, seed, assigned = None):
        self.team_name = team_name
        self.group = group
        self.world_rank = world_rank
        self.seed = seed
        self.assigned = assigned

    def make_team_dict(self):
        team_dict = {"team_name":self.team_name,
        "world_rank": self.world_rank,
        "group": self.group,
        "seed": self.seed,
        "assigned":self.assigned}

        return team_dict

