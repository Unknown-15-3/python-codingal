import pandas as pd
import numpy as np
exam_data = {
    "Name" : ["Anna", "Diara", "Jacob", "Mark", "Luna", "Maya", "Robert", "Xander", "Jiya", "Daniel"],
    "score": [12, 17, 18, 15, 10, np.nan, 14, 19, 20, 11],
    "attempt": [1, 3,1, 3, 4, 2, 1, 1, 3, 2],
    "qualify": ["yes","no","yes","no","no","no","yes","yes","no","no"]
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index = labels)
print("summary of the basic information about this dataframe and its data:-")
print(df.info())