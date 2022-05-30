def radar_plot(tournament, team, position, name):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import highlight_text
    import matplotlib.font_manager
    import base64
    import math
    from scipy import stats
    import numpy as np
    import time
    import os
    from transferPredict.settings import BASE_DIR

    file_path = os.path.join(BASE_DIR, 'transferPredictApp/who_scored.csv')
    df = pd.read_csv(file_path)

    background = "#444444"
    text_color = 'w'
    primary='red'
    mpl.rcParams['xtick.color'] = text_color
    mpl.rcParams['ytick.color'] = text_color
    title_font = 'Perpetua'
    body_font = 'Open Sans'

    try:
        player_value = df[(df.Tournament == tournament)&(df.Team == team)&(df.Position == position)\
            &(df.Name == name)]
        others_value = df[(df.Tournament == tournament)&(df.Position == position)]
    except:
        player_value = 0
        others_value = 0

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

    values = player_value[attributes].values
    others_values = others_value[attributes]

    values_perc = [stats.percentileofscore(others_values.iloc[:,x].values, values[0][x]) for x in range(len(values[0]))]
    values_perc = [*values_perc, values_perc[0]]
    attributes = [*attributes, attributes[0]]

    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(values_perc))

    fig, ax = plt.subplots(figsize=(6,4), subplot_kw=dict(polar=True))

    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)

    ax.grid(ls='dotted', lw='0.5', color='lightgray', zorder= 1)

    highlight_textprops =\
    [{"color": primary, "fontsize":12, "fontfamily":title_font, "fontweight":'bold'},
    {"color": text_color, "fontsize":12, "fontfamily":title_font, "fontweight":'bold'},
    {"color": text_color, "fontsize":10, "fontfamily":body_font}]

    highlight_text.fig_text(x=0.02, y=0.99,
                s=f"<{name}'s> <stats compared to other {position.lower()}s>\n<{tournament} - 2019/2020>",
                highlight_textprops=highlight_textprops)

    ax.plot(label_loc, values_perc, label=name, linewidth=1, color=primary)
    ax.fill(label_loc, values_perc, color=primary, alpha=0.25)

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
    
    radar_fig_path = os.path.join(BASE_DIR, 'transferPredictApp/radar_plot.png')
    plt.savefig(radar_fig_path, format='png')
    time.sleep(1)
    with open(radar_fig_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    return encoded_string.decode("utf-8")
