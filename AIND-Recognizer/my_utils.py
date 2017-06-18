import numpy as np

def add_ground_features_to_dataframe(df):
    """
    Calculate the ground values for left, right and x,y
    it use the variable - nose formula to calculate ground

    Parameters
    ----------
    df : DataFrame
        dataset in form of DataFrame

    Returns
    -------
        Add the ground value to the same object
    """
    df['grnd-ry'] = df['right-y'] - df['nose-y']
    df['grnd-rx'] = df['right-x'] - df['nose-x']
    df['grnd-ly'] = df['left-y']  - df['nose-y']
    df['grnd-lx'] = df['left-x']  - df['nose-x']


def std_by_speaker(df):
    """
    Calculate the standard diviation for data frame passed in based on each speaker

    Parameters
    ----------
    df : DataFrame
        dataset in form of DataFrame    

    Returns
    -------
    DataFrame
        standard diviation value for each feature calculated per each speaker
    """
    return df.groupby('speaker').std()



def add_normalized_features_to_dataframe(df, df_means, df_std):
    """
    Add features for normalized by speaker values of left, right, x, y
    Name these 'norm-rx', 'norm-ry', 'norm-lx', and 'norm-ly'
    using Z-score scaling. foprmula: (X-Xmean)/Xstd

    Parameters
    ----------
    df : DataFrame
        dataset in form of DataFrame

    Returns
    -------
        Add the normalized value to the same object
    """   
    df['norm-rx'] = (df['right-x'] - df['speaker'].map(df_means['right-x'])) / df['speaker'].map(df_std['right-x'])
    df['norm-ry'] = (df['right-y'] - df['speaker'].map(df_means['right-y'])) / df['speaker'].map(df_std['right-y'])
    df['norm-lx'] = (df['left-x']  - df['speaker'].map(df_means['left-x']))  / df['speaker'].map(df_std['left-x'])
    df['norm-ly'] = (df['left-y']  - df['speaker'].map(df_means['left-y']))  / df['speaker'].map(df_std['left-y'])

def add_polar_features_to_dataframe(df):
    """
    add features for polar coordinate values where the nose is the origin
    Name these 'polar-rr', 'polar-rtheta', 'polar-lr', and 'polar-ltheta'
    Note that 'polar-rr' and 'polar-rtheta' refer to the radius and angle

    Parameters
    ----------
    df : DataFrame
        dataset in form of DataFrame

    Returns
    -------
        Add the polar coordinate values to the same object
    """     
    grnd_rx = df['grnd-rx']
    grnd_ry = df['grnd-ry']
    grnd_lx = df['grnd-lx']
    grnd_ly = df['grnd-ly']

    df['polar-rr']      = np.sqrt(   grnd_rx * grnd_rx + grnd_ry * grnd_ry)
    df['polar-lr']      = np.sqrt(   grnd_lx * grnd_lx + grnd_ly * grnd_ly)
    df['polar-rtheta']  = np.arctan2(grnd_rx, grnd_ry)
    df['polar-ltheta']  = np.arctan2(grnd_lx, grnd_ly)


def add_delta_features_to_dataframe(df):
    """
    Add delta of right-x, right-y, left-x, and left-y
    Name these 'delta-rx', 'delta-ry', 'delta-lx', 'delta-ly'    

    Parameters
    ----------
    df : DataFrame
        dataset in form of DataFrame

    Returns
    -------
        Add the delta of values to the same object
    """ 
    df['delta-rx'] = df['right-x'].diff().fillna(0)
    df['delta-ry'] = df['right-y'].diff().fillna(0)
    df['delta-lx'] = df['left-x'] .diff().fillna(0)
    df['delta-ly'] = df['left-y'] .diff().fillna(0)
