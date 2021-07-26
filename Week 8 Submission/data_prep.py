import pandas as pd

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

    # Writing the dataframe into a new cleaned up data_set that we can use
    df.to_csv(target_filename, index=False)
