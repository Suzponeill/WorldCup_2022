import csv
from Models.Team import Team
from Models.Participant import Participant
import json
import random


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


Participant_names = ["Patrick","Suz","John","Hugh","Brad","Diane","Nate","Jordan"]

participant_list = [Participant(name) for name in Participant_names]
participant_dicts_list = [participant.participant_dict() for participant in participant_list]
# print(json.dumps(participant_dicts_list, indent=2))


def assign_draft_position(list_participant_instances):
    draft_positions = list(range(1, 9))
    for participant in list_participant_instances:
        position = random.choice(draft_positions)
        participant.draft_position = position
        # print(participant.participant_dict())
        draft_positions.remove(position)
    
    participant_dicts_list = [participant.participant_dict() for participant in list_participant_instances]

    return participant_dicts_list
    


def draft_teams(participant_instance_list, teams_list):
    seed = 1

    while seed < 5:
        # reverse the draft order on each iteration
        if seed % 2 != 0:
            participant_instance_list = sorted(participant_instance_list, key=lambda x: x.draft_position, reverse=False)
        else:
            participant_instance_list = sorted(participant_instance_list, key=lambda x: x.draft_position, reverse=True)
        
        # Iterate over participants
        for participant in participant_instance_list:

            participant_groups = []
            for team in participant.teams_list:
                for group in team.group:
                    participant_groups.append(group)

            # Determine the best team to assign to the participant in the given seed
            available_teams = list(filter(lambda x: not x.assigned, teams_list))
            available_teams_in_seed = list(filter(lambda y: (y.seed==seed), available_teams))
            available_teams_in_seed_no_repeat_groups = list(filter(lambda z: (z.group not in participant_groups), available_teams_in_seed))
            if len(available_teams_in_seed_no_repeat_groups) == 0:
                return f"No solution without repeat groups."

            best_available_team = min(available_teams_in_seed_no_repeat_groups, key=lambda x: x.world_rank)
            participant.teams_list.append(best_available_team)
            best_available_team.assigned = participant.name   
        seed += 1

    participant_dicts_list = [participant.participant_dict() for participant in participant_instance_list]
    return participant_dicts_list

                    
assign_draft_position(participant_list)


print(json.dumps(draft_teams(participant_list, teams_list), indent=2))


# print(json.dumps(([team.make_team_dict() for team in teams_list]), indent=2))


