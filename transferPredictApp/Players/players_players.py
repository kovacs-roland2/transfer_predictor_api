def players_players(tournament, team, position):
    import pandas as pd
    import os 
    from transferPredict.settings import BASE_DIR

    file_path = os.path.join(BASE_DIR, 'transferPredictApp/who_scored.csv')
    df = pd.read_csv(file_path)

    return sorted(list(set(df[(df.Tournament == tournament)&(df.Team == team)&(df.Position == position)].Name.values)))
