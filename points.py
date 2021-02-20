import re


def extract_multiplier(data):
    """ Function looks for validly formatted points multipliers and
    converts to a number """

    pattern = r"\(X(\d)\)$"
    match = re.search(pattern, data)

    if  match:
        mult = int(match.group(1))
        
    else:
        mult = 0
    
    return mult



def strip_mult(df):
    """ Function strips the regex-matched multipliers from a
    Pandas DF"""

    return df[0].replace(r'\s\(X(\d)\)$', '', regex=True)



def process_points(df):
    """ Function extracts the multipliers from the heading column
    converts to a number, adds columns for points values, and 
    scales by the multiplier. Takes a Pandas dataframe of the table
    as input """

    mults = []

    for idx, row in df.iterrows():
        mults.append( extract_multiplier(row[0]) )
        print(row[0])

    df['min_pts'] = mults
    df['max_pts'] = mults

    df['min_pts'] = df['min_pts'] * 1
    df['max_pts'] = df['max_pts'] * 10

    return df
