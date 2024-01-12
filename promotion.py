import pandas as pd

def promote(file):
    
    """ 
    This modul offers basic functionality of move pupils up one grade.
    All that is left to do is to elegantly loop over all entries (classes)
    and move them up one grade
    It is critical that the class column is named "klasse" and the format is "integer+letter" 
    """
    # Write code to access uploaded file here
    data = ""

    df = pd.read_csv(file) #read uploaded file
    df.loc[df["klasse"] == "11a", "klasse"] = "12a"    
    df.loc[df["klasse"] == "11b", "klasse"] = "12b"
    df.loc[df["klasse"] == "11c", "klasse"] = "12c"
    df.loc[df["klasse"] == "11d", "klasse"] = "12d"
    df.loc[df["klasse"] == "10a", "klasse"] = "11a"
    df.loc[df["klasse"] == "10b", "klasse"] = "11b"
    df.loc[df["klasse"] == "10c", "klasse"] = "11c"
    df.loc[df["klasse"] == "10d", "klasse"] = "11d"
    df.loc[df["klasse"] == "9a", "klasse"] = "10a"
    df.loc[df["klasse"] == "9b", "klasse"] = "10b"
    df.loc[df["klasse"] == "9c", "klasse"] = "10c"
    df.loc[df["klasse"] == "9d", "klasse"] = "10d"
    df.loc[df["klasse"] == "8d", "klasse"] = "9d"
    df.loc[df["klasse"] == "8a", "klasse"] = "9a"
    df.loc[df["klasse"] == "8b", "klasse"] = "9b"
    df.loc[df["klasse"] == "8c", "klasse"] = "9c"
    df.loc[df["klasse"] == "7a", "klasse"] = "8a"
    df.loc[df["klasse"] == "7b", "klasse"] = "8b"
    df.loc[df["klasse"] == "7c", "klasse"] = "8c"
    df.loc[df["klasse"] == "7d", "klasse"] = "8d"
    df.loc[df["klasse"] == "6a", "klasse"] = "7a"
    df.loc[df["klasse"] == "6b", "klasse"] = "7b"
    df.loc[df["klasse"] == "6c", "klasse"] = "7c"
    df.loc[df["klasse"] == "6d", "klasse"] = "7d"
    df.loc[df["klasse"] == "5a", "klasse"] = "6a"
    df.loc[df["klasse"] == "5b", "klasse"] = "6b"
    df.loc[df["klasse"] == "5c", "klasse"] = "6c"
    df.loc[df["klasse"] == "5d", "klasse"] = "6d"
    df.loc[df["klasse"] == "4a", "klasse"] = "5a"
    df.loc[df["klasse"] == "4b", "klasse"] = "5b"
    df.loc[df["klasse"] == "4c", "klasse"] = "5c"
    df.loc[df["klasse"] == "4d", "klasse"] = "5d"
    df.loc[df["klasse"] == "3a", "klasse"] = "4a"
    df.loc[df["klasse"] == "3b", "klasse"] = "4b"
    df.loc[df["klasse"] == "3c", "klasse"] = "4c"
    df.loc[df["klasse"] == "3d", "klasse"] = "4d"
    df.loc[df["klasse"] == "2a", "klasse"] = "3a"
    df.loc[df["klasse"] == "2b", "klasse"] = "3b"
    df.loc[df["klasse"] == "2c", "klasse"] = "3c"
    df.loc[df["klasse"] == "2d", "klasse"] = "3d"
    df.loc[df["klasse"] == "1a", "klasse"] = "2a"
    df.loc[df["klasse"] == "1b", "klasse"] = "2b"
    df.loc[df["klasse"] == "1c", "klasse"] = "2c"
    df.loc[df["klasse"] == "1d", "klasse"] = "2d"
    df.loc[df["klasse"] == "2d", "klasse"] = "3d"
    
    print("Pupils promoted!")
    df.to_csv("./static/download/data-delta.csv", encoding='utf-8', index=False) #write mutated data to csv file
    #df_delta = pd.read_csv('./test-data-delta.csv')