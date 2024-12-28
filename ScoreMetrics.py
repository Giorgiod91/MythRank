import json

score_range_based_on_dps= {

    "DPS" 
    "Category": [
        "Needs to learn" ,
        "Mid Range Dps" ,
        "Average Dps Output",
        "High Dps Output" ,
       
    ]
}

#hardcoded data for now 

logs = [
    {"DPS": 4200, "Interrupts": 5, "Deaths": 0, "Crowd_control": 2, "Pots_used": 1},
    {"DPS": 4100, "Interrupts": 4, "Deaths": 1, "Crowd_control": 3, "Pots_used": 1},
    {"DPS": 1300, "Interrupts": 6, "Deaths": 0, "Crowd_control": 2, "Pots_used": 2},
]




#get player id from the file 

def get_local_player_id():
    try:
        # Read the id from the file
        with open(".ids", mode="r", encoding="utf-8") as f:
            player_id = json.load(f)
            return player_id['id']  
    except OSError as e:
        print(f"Error reading id: {e}")
        return None
    



#get the values i need for define score metrics 


# defining the values from the parameters for the score syste, like dps interrupts and so on and how much weight they have
def define_score_metrics_weight(logs, dps_weight=60, interrupt_weight=10, death_weight=10, cc_weight=10, pots_weight=10):
    score_range = {
        "0-500": "Rank: Beginner",
        "501-1000": "Rank: Intermediate",
        "1001-1500": "Rank: Advanced",
        "1501-2000": "Rank: Pro",
        "2001-2500": "Rank: Elite",
        "2501-3000": "Rank: Master",
        "3001+": "Rank: Legendary"
    }
   
   
    if len(logs) < 5: 
       
        exit

    # Initialize totals for each metric
    total_dps = 0
    total_interrupts = 0
    total_deaths = 0
    total_cc = 0
    total_pots = 0

    # Sum all the logs
    for log in logs:
        total_dps += log.get("DPS", 0)
        total_interrupts += log.get("Interrupts", 0)
        total_deaths += log.get("Deaths", 0)
        total_cc += log.get("Crowd_control", 0)
        total_pots += log.get("Pots_used", 0)

    # Calculate averages
    num_logs = len(logs)
    avg_dps = total_dps / num_logs
    avg_interrupts = total_interrupts / num_logs
    avg_deaths = total_deaths / num_logs
    avg_cc = total_cc / num_logs
    avg_pots = total_pots / num_logs

    # Calculate the weighted score
    #TODO: rethink the minus score on deaths 
    weighted_score = (
        (avg_dps * dps_weight / 100) +
        (avg_interrupts * interrupt_weight / 100) -
        (avg_deaths * death_weight / 100) +  #minus here cause deaths should remove the score for now
        (avg_pots * pots_weight / 100)
    )

    if weighted_score <= 500:
        return score_range["0-500"]
    elif weighted_score <= 1000:
        return score_range["501-1000"]
    elif weighted_score <= 1500:
        return score_range["1001-1500"]
    elif weighted_score <= 2000:
        return score_range["1501-2000"]
    elif weighted_score <= 2500:
        return score_range["2001-2500"]
    elif weighted_score <= 3000:
        return score_range["2501-3000"]
    else:
        return score_range["3001+"]
        
    

result = define_score_metrics_weight(logs)
print(result)



def get_player_Score(id, score):
    if score <= 500:
        return score_range["0-500"]
    elif score <= 1000:
        return score_range["501-1000"]
    elif score <= 1500:
        return score_range["1001-1500"]
    elif score <= 2000:
        return score_range["1501-2000"]
    elif score <= 2500:
        return score_range["2001-2500"]
    elif score <= 3000:
        return score_range["2501-3000"]
    else:
        return score_range["3001+"]
