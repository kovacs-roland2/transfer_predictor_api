def similarity_plot(position, name):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import highlight_text
    import matplotlib.font_manager
    import base64
    import math
    from scipy import stats
    import numpy as np
    import json
    import joblib
    from sklearn.metrics.pairwise import cosine_similarity
    import os
    from transferPredict.settings import BASE_DIR

    file_path = os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/ws_sim_player.csv')
    df_cluster = pd.read_csv(file_path)
    player_df = df_cluster[df_cluster.NewName_x == name].drop(['Unnamed: 0', 'NewName_x', 'playerId', 'positionText_x', 'Year', 'Year_x', 'Year_y',\
        'teamName_x', 'League_x'], axis = 1)

    if position == 'Goalkeeper':
        df_columns = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/df_columns_goalkeeper.csv'))
        df_columns = df_columns.drop('Unnamed: 0', axis = 1)
        df_clust = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/ws_sim_goalkeeper.csv'))
        df_clust = df_clust.drop('Unnamed: 0', axis = 1)
        pca = joblib.load(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Models/pca_goalkeeper.sav'))
    elif position == 'Defender':
        df_columns = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/df_columns_defender.csv'))
        df_columns = df_columns.drop('Unnamed: 0', axis = 1)
        df_clust = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/ws_sim_defender.csv'))
        df_clust = df_clust.drop('Unnamed: 0', axis = 1)
        pca = joblib.load(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Models/pca_defender.sav'))
    elif position == 'Midfielder':
        df_columns = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/df_columns_midfielder.csv'))
        df_columns = df_columns.drop('Unnamed: 0', axis = 1)
        df_clust = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/ws_sim_midfielder.csv'))
        df_clust = df_clust.drop('Unnamed: 0', axis = 1)
        pca = joblib.load(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Models/pca_midfielder.sav'))
    else:
        df_columns = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/df_columns_Forward.csv'))
        df_columns = df_columns.drop('Unnamed: 0', axis = 1)
        df_clust = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/ws_sim_Forward.csv'))
        df_clust = df_clust.drop('Unnamed: 0', axis = 1)
        pca = joblib.load(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Models/pca_Forward.sav'))

    player_df = pca.transform(player_df)    

    sim_index = cosine_similarity(player_df, df_clust)

    df_columns['sim'] = sim_index[0]
    df_columns['sim'] = round(df_columns['sim'], 2)

    df_columns = df_columns.drop(['playerId', 'positionText_x', 'index'], axis = 1)
    df_columns = df_columns.rename(columns={'League_x': 'League',
                    'NewName_x': 'Name', 'teamName_x': 'Team', 'sim':'Similarity'})
    df_columns = df_columns.drop_duplicates()
    df_columns = df_columns.sort_values(by='Similarity', ascending=False)[:11]
    df_columns2 = df_columns.iloc[1:11]

    tournaments = df_columns[:6]['League'].values
    teams = df_columns[:6]['Team'].values
    names = df_columns[:6]['Name'].values

    df_21 = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Similarity/Data/df_21.csv'))

    background = "#444444"
    text_color = 'w'
    primary='red'
    mpl.rcParams['xtick.color'] = text_color
    mpl.rcParams['ytick.color'] = text_color
    title_font = 'Perpetua'
    body_font = 'Open Sans'

    colors = [primary, '#edf4ff', '#97c1ff', '#408Bfc', '#054ada', '#061f80']

    if position == 'Goalkeeper':
        attributes = ['Pass success rate', 'Saves (six yard box)', 'Saves (penalty area)',\
            'Saves (out of the box)', 'Saves total']
    elif position == 'Defender':
        attributes = ['Pass success rate', 'Passes', 'Aerials won', 'Aerials lost',\
                'Tackles', 'Interceptions', 'Clearances', 'Blocks', 'Challenges lost']
    elif position == 'Midfielder':
        attributes = ['Tackles', 'Interceptions', 'Pass success rate',\
                'Keypasses', 'Passes', 'Accurate crosses', 'Dribbles won',\
                'Shots total', 'Goals', 'Assists']
    elif position == 'Forward':
        attributes = ['Passes', 'Keypasses',\
            'Dribbles won',\
            'Shots total', 'Shots on target',\
            'Aerials won', 'Goal open play','Goals', 'Assists']

    fin_values = []
    for i in range(len(names)):
        player_value = df_21[(df_21.League == tournaments[i])&(df_21.teamName == teams[i])&(df_21.positionText == position)\
            &(df_21.NewName == names[i])]
        others_value = df_21[(df_21.League == tournaments[i])&(df_21.positionText == position)]

        values = player_value[attributes].values
        others_values = others_value[attributes]

        values_perc = [stats.percentileofscore(others_values.iloc[:,x].values, values[0][x]) for x in range(len(values[0]))]
        values_perc = [*values_perc, values_perc[0]]
        fin_values.append(values_perc)



    attributes = [*attributes, attributes[0]]

    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(values_perc))

    fig, ax = plt.subplots(figsize=(6,5), subplot_kw=dict(polar=True))

    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)

    ax.grid(ls='dotted', lw='0.5', color='lightgray', zorder= 1)

    for fin_value, color, n in zip(fin_values,colors, names):
        ax.plot(label_loc, fin_value, label=n, linewidth=1, color=color)
        ax.fill(label_loc, fin_value, color=color, alpha=0.25)

    # Fix axis to go in the right order and start at 12 o'clock.
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Draw axis lines for each angle and label.
    ax.set_thetagrids(np.degrees(label_loc), labels=attributes)

    # Go through labels and adjust alignment based on where
    # it is in the circle.
    for label, angle in zip(ax.get_xticklabels()[:-1], label_loc[:-1]):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')

    # Ensure radar goes from 0 to 100.
    ax.set_ylim(0, 100)

    # Add some custom styling.
    # Change the color of the tick labels.
    ax.tick_params(colors='w')
    # Make the y-axis (0-100) labels smaller.
    ax.tick_params(axis='y', labelsize=8, color='w')
    # Change the color of the circular gridlines.
    ax.grid(ls='dotted', lw='0.5', color='lightgrey', zorder= 1)
    # Change the color of the outermost gridline (the spine).
    ax.spines['polar'].set_color('w')
    # Change the background color inside the circle itself.
    ax.set_facecolor(background)

    ax.legend(labelcolor='w', facecolor='#444444', edgecolor='#444444', ncol=3, loc='lower center', bbox_to_anchor=(0.5, -0.3), fontsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(BASE_DIR, 'transferPredictApp/similarity_plot.png'), format='png')
    with open(os.path.join(BASE_DIR, 'transferPredictApp/similarity_plot.png'), "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return (encoded_string.decode("utf-8"), df_columns2.to_dict('records'))