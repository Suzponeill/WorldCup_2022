import csv
from Models.Team import Team
from Models.Participant import Participant
import json


teams_list = []

with open('World_Cup_Teams.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None) #skip the header.
    #unpack the row directly in the head of the for loop
    for team_name, group, world_rank, seed in reader:
        team_name = str(team_name)
        group = str(group)
        world_rank = int(world_rank)
        seed = int(seed)
        #Now create the Team instance and append it to the list
        team_instance = (Team(team_name, group, world_rank, seed))
        teams_list.append(team_instance)

teams_dicts_list = [team.make_team_dict() for team in teams_list]
# print(json.dumps(teams_dicts_list, indent=2))


Participant_names = ["Patrick","Suz","John","Sommer","Brad","Diane","Nate","Jordan"]

participant_list = [Participant(name) for name in Participant_names]
participant_dicts_list = [participant.participant_dict() for participant in participant_list]
# print(json.dumps(participant_dicts_list, indent=2))