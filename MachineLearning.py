import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# hardcoded data for testing now later will be using real fetched data from the player id
data = {
    "DPS": list(range(0, 101)),  
    "Category": [
        "Needs to learn" if x <= 79 else
        "Mid Range Dps" if x <= 90 else
        "Average Dps Output" if x <= 96 else
        "High Dps Output" if x <= 99 else
        "Dps Machine"
        for x in range(0, 101)
    ]
}





dummy = [ 99, 87 , 98 , 99 ,99]








