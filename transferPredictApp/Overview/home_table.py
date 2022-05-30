def home_table(tournament, position):
    import pandas as pd
    import os
    from transferPredict.settings import BASE_DIR

    file_path = os.path.join(BASE_DIR, 'transferPredictApp/who_scored.csv')
    df = pd.read_csv(file_path)

    if tournament != 'Top 5':
        df = df[df.Tournament == tournament]

    if position == 'standard':
        df = df[['Name', 'Team', 'Tournament', 'Age', 'Position', 'Apps', 'Sub on',\
                'Minutes played', 'Rating', 'MOTM', 'Goals total', 'Assists total', 'Yellow cards',	'Red cards']]
    elif position == 'goalkeeper':
        df = df[df.Position == 'Goalkeeper']
        df = df[['Name', 'Team', 'Tournament', 'Age', 'Pass success rate', 'Saves (six yard box)', 'Saves (penalty area)',\
            	'Saves (out of the box)', 'Saves total']]
    elif position == 'defender':
        df = df[df.Position == 'Defender']
        df = df[['Name', 'Team', 'Tournament', 'Age', 'Pass success rate', 'Passes', 'Aerials won', 'Aerials lost',\
             'Tackles', 'Interceptions', 'Clearances', 'Blocks', 'Challenges lost']]
    elif position == 'midfielder':
        df = df[df.Position == 'Midfielder']
        df = df[['Name', 'Team', 'Tournament', 'Age', 'Pass success rate', 'Pass success rate',	'Tackles', 'Interceptions',	'Clearances',\
            	'Blocks', 'Keypasses', 'Dribbles won', 'Dispossessed', 'Turnovers', 'Passes', 'Accurate crosses', 'Accurate long passes',\
                    	'Accurate through balls', 'Shots total', 'Shots on target',	'Goals', 'Dribbles total', 'Assists']]
    elif position == 'attacker':
        df = df[df.Position == 'Forward']
        df = df[['Name', 'Team', 'Tournament', 'Age', 'Pass success rate', 'Passes', 'Pass success rate', 'Keypasses',\
            'Dribbles won',	'Fouls given', 'Offsides given', 'Dispossessed', 'Turnovers', 'Passes',	'Shots (penalty area)',\
                'Shots (outside of the box)', 'Shots total', 'Shots on target', 'Shots off target',	'Shots on post', 'Shots blocked',\
                    'Shots header',	'Goal (six yard box)', 'Goal (penalty area)', 'Goal (outside of the box)', 'Goals',\
                        'Goal open play', 'Goals head',	'Aerials won', 'Assists']]

    return df.to_dict()