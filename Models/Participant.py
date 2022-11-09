class Participant:

    def __init__(self, name, draft_position = 0, teams_list = None):
        self.name = name
        self.draft_position = draft_position
        if teams_list is None:
            self.teams_list = []
    
    def participant_dict(self):
        participant_dict = {"name":self.name,
        "draft_position":self.draft_position}
 
        teams_dict_list = []
        for team in self.teams_list:
            team_dict = {"team_name":team.team_name,
                "world_rank": team.world_rank,
                "group": team.group,
                "seed": team.seed,
                "assigned":team.assigned}
            teams_dict_list.append(team_dict)
        participant_dict["teams_list"] = teams_dict_list

        

        return participant_dict
        
