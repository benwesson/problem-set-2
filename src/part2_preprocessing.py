'''
PART 2: Pre-processing
- Take the time to understand the data before proceeding
- Load `pred_universe_raw.csv` into a dataframe and `arrest_events_raw.csv` into a dataframe
- Perform a full outer join/merge on 'person_id' into a new dataframe called `df_arrests`
- Create a column in `df_arrests` called `y` which equals 1 if the person was arrested for a felony crime in the 365 days after their arrest date in `df_arrests`. 
- - So if a person was arrested on 2016-09-11, you would check to see if there was a felony arrest for that person between 2016-09-12 and 2017-09-11.
- - Use a print statment to print this question and its answer: What share of arrestees in the `df_arrests` table were rearrested for a felony crime in the next year?
- Create a predictive feature for `df_arrests` that is called `current_charge_felony` which will equal one if the current arrest was for a felony charge, and 0 otherwise. 
- - Use a print statment to print this question and its answer: What share of current charges are felonies?
- Create a predictive feature for `df_arrests` that is called `num_fel_arrests_last_year` which is the total number arrests in the one year prior to the current charge. 
- - So if someone was arrested on 2016-09-11, then you would check to see if there was a felony arrest for that person between 2015-09-11 and 2016-09-10.
- - Use a print statment to print this question and its answer: What is the average number of felony arrests in the last year?
- Print the mean of 'num_fel_arrests_last_year' -> pred_universe['num_fel_arrests_last_year'].mean()
- Print pred_universe.head()
- Return `df_arrests` for use in main.py for PART 3; if you can't figure this out, save as a .csv in `data/` and read into PART 3 in main.py
'''

# import the necessary packages
import pandas as pd
import numpy as np
from datetime import timedelta
 # Your code here
def part_2_function():
   
    #Read CSVs
    pred_universe_raw = pd.read_csv("data/pred_universe_raw.csv")
    arrest_events_raw = pd.read_csv("data/arrest_events_raw.csv")

    #Join dataframes
    df_arrests = pd.merge(pred_universe_raw,arrest_events_raw,how = "outer",on = ["person_id"])

    #convert string dates to datetime dates
    df_arrests["arrest_date_event"] = pd.to_datetime(df_arrests["arrest_date_event"])
    df_arrests["arrest_date_univ"] = pd.to_datetime(df_arrests["arrest_date_univ"])
    
    #Create column y
    df_arrests["y"] = np.where(df_arrests["arrest_date_univ"] < (df_arrests["arrest_date_event"] + timedelta(days=365)),1,0)
    df_arrests.to_csv("data/df_arrests.csv")


    #print(df_arrests)
    x = df_arrests["y"].value_counts()
    
    print("Percentage of people arrested for crime within a year",x[1]/6519)
    y = df_arrests["charge_degree"].value_counts()
    print("The amount of current charges that are felonies are",y["felony"])
    return df_arrests

print(part_2_function())
