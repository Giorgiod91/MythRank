import json

score_range = {
    "0-500": "red",
    "501-1000": "orange",
    "1001-1500": "yellow",
    "1501-2000": "green",
    "2001-2500": "blue",
    "2501-3000": "purple",
    "3001+": "gold"
}

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
def get_metrics_values():
    try:




    return DPS, Interrupts, Deaths, Crowd_control, Pots_used

# defining the values from the parameters for the score syste, like dps interrupts and so on and how much weight they have
def define_score_metrics_weight(DPS, Interrupts, Deaths, Crowd_control, Pots_used, ):
    full_weight_value = 0

    # setting a min value so that the player needs at least 5 logs from runs to be considered beeing ranked 
    min_data_required = 5
    if(min_data_required < 5):
        exit

    #ranking dps high for now
    DPS = full_weight_value / 100 * 60
    Interrupts = full_weight_value / 100 * 10
    Deaths = full_weight_value / 100 * 10
    Crowd_control = full_weight_value / 100 * 10
    Pots_used = full_weight_value / 100 * 10
    full_weight_value = DPS + Interrupts + Deaths + Crowd_control + Pots_used
    
    return full_weight_value


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
