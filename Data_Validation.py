import pandas as pd
import re
import math
import os

def completness_ratio(df):
    "This function computes the data completness ratio for each variable in the dataframe"
    completeness_ratios = (1 - df.isnull().mean()) * 100
    completeness_df = pd.DataFrame({
        'Variable': completeness_ratios.index,
        'Completeness_Ratio': completeness_ratios.values
    })
    return completeness_df

note_file = os.path.join("data", "notes.txt")


def identify_regex_type(s):
    """This function identifies the data type of a data point"""

    if isinstance(s, float) and math.isnan(s) or s == ' ':
        return 'Null'
    
    patterns = {
        'Numerical': r'^\d+$',
        'Alphabetical': r'^[a-zA-Z]+$',
        'Alphanumeric': r'^[a-zA-Z0-9]+$',
    }
    
    for pattern_type, pattern in patterns.items():
        if re.match(pattern, s):
            return pattern_type
    
    return 'Unknown'



def data_val_erroneous(df):
    """The function checks for object variable columns if the data type is consistent within the column."""
    object_columns = [idx for idx, dtype in enumerate(df.dtypes) if dtype == 'object']
    inconsistent_columns = []

    for i in object_columns:
        first_regex = identify_regex_type(df.iloc[:, i][0])
        
        for obs in df.iloc[:, i]:
            obs_regex = identify_regex_type(obs)
            if (obs_regex != first_regex and obs_regex != 'Null' and first_regex != 'Null'):
                inconsistent_columns.append((df.columns[i], first_regex, obs_regex))
                break
        
    if not inconsistent_columns:
        return "All data types are consistent across object columns."
    else:
        inconsistent_details = "; ".join(
            [f"Column '{col}' may have inconsistent data types: {first_regex} and {inconsistent_regex}" 
             for col, first_regex, inconsistent_regex in inconsistent_columns]
        )
        return f"Inconsistent data types found: {inconsistent_details}"
    
    
def data_val_duplicates(df):
    """This function check for any duplicates and returns the number of duplicates in the dataset"""
    no_duplicated_rows = df.duplicated().sum()
    return f" The dataset contains {no_duplicated_rows} duplicates"

