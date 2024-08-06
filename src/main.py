'''
You will run this problem set from main.py, so set things up accordingly
'''

import pandas as pd
import numpy as np
from datetime import timedelta
import part1_etl
import part2_preprocessing
import part3_logistic_regression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedKFold as KFold_strat
from sklearn.linear_model import LogisticRegression as lr

# Call functions / instanciate objects from the .py files
def main():

    # PART 1: Instanciate etl, saving the two datasets in `./data/`
    print(part1_etl.getFiles())
    # PART 2: Call functions/instanciate objects from preprocessing
    print(part2_preprocessing.part_2_function())
    # PART 3: Call functions/instanciate objects from logistic_regression
    print(part3_logistic_regression.logFunction())
    # PART 4: Call functions/instanciate objects from decision_tree

    # PART 5: Call functions/instanciate objects from calibration_plot


if __name__ == "__main__":
    main()