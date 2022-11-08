class Participant:

    def __init__(self, name, draft_position = 0, teams_list = None):
        self.name = name
        self.draft_position = draft_position
        self.teams_list = teams_list
    
    def participant_dict(self):
        participant_dict = {"name":self.name,
        "draft_position":self.draft_position,
        "teams_list":self.teams_list}

        return participant_dict
        
