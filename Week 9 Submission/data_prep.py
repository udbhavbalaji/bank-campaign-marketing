import pandas as pd
import numpy as np

def clean_data(filename, target_filename, sep, na):
    # Reading in the full data
    df = pd.read_csv(filename, sep=sep, na_values=na)

    # Correcting the columns names
    cols = df.columns
    column = []
    for col in cols:
        if '.' in col:
            words = col.split('.')
            actual_col = ''
            for i in range(len(words)):
                if i == len(words)-1:
                    actual_col += words[i]
                else:
                    actual_col += words[i]+'_'
            column.append(actual_col)
        else:
            column.append(col)
    df.columns = column

    # Cleaning out the data as per decisions taken in Week 8

    ## Imputing NaN Values

    ### Column: JOB ; Method of Imputing NaN Values: Mode
    df['job'] = df['job'].fillna(df['job'].mode()[0])

    ### Column: MARITAL ; Method of Imputing NaN Values: Mode
    df['marital'] = df['marital'].fillna(df['marital'].mode()[0])

    ### Column: EDUCATION ; Method of Imputing NaN Values: Creating a N/A category because there are a lot of missing values
    df['education'].fillna(na, inplace=True)

    ### Column: DEFAULT ; Method of Imputing NaN Values: Mode
    df['default'] = df['default'].fillna(df['default'].mode()[0])

    ### For HOUSING and LOAN columns, we can just drop the rows with NaN values as it would not affect the dataset too much
    df.dropna(axis=0, how='any', inplace=True)

    ## Replacing the 999 value in PDAYS with a 0
    df['pdays'] = df['pdays'].replace([999],0)

    ## Dropping duplicates
    df.drop_duplicates(keep='first', inplace=True)

    ## Dealing with outliers in the AGE column
    q1 = df['age'].quantile(0.25)
    q3 = df['age'].quantile(0.75)
    iqr = q3 - q1
    lower_outlier = df["age"]< (q1-1.5*iqr)
    upper_outlier = df["age"] > (q3+1.5*iqr)
    df_final = df[~(lower_outlier | upper_outlier)]

    # Writing the dataframe into a new cleaned up data_set that we can use
    df_final.to_csv(target_filename, index=False)

if __name__ == "__main__":
    clean_data('Data/bank_additional_full.csv','Data/bank_data.csv',';','unknown')
