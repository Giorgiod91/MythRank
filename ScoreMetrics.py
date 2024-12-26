data = []

score_range = {
    "0-500": "red",
    "501-1000": "orange",
    "1001-1500": "yellow",
    "1501-2000": "green",
    "2001-2500": "blue",
    "2501-3000": "purple",
    "3001+": "gold"
}

# defining the values from the parameters for the score syste, like dps interrupts and so on and how much weight they have
def define_score_metrics_weight():
    full_weight_value = 0   
    #ranking dps high for now
    DPS = full_weight_value / 100 * 60
    Interrupts = full_weight_value / 100 * 10
    Deaths = full_weight_value / 100 * 10
    Crowd_control = full_weight_value / 100 * 10
    Pots_used = full_weight_value / 100 * 10
    full_weight_value = DPS + Interrupts + Deaths + Crowd_control + Pots_used
    
    return full_weight_value

