def get_player_info(tournament, team, position, name):
    import pandas as pd
    import os
    from transferPredict.settings import BASE_DIR

    file_path = os.path.join(BASE_DIR, 'transferPredictApp/who_scored.csv')
    df = pd.read_csv(file_path)
    
    df =  df[(df.Tournament == tournament)&(df.Team == team)&\
        (df.Position == position)&(df.Name == name)][['Name', 'Team', 'Position', 'Age', 'Apps', 'Rating', 'Goals total', 'Assists total']]
        
    return df.to_dict()
   
