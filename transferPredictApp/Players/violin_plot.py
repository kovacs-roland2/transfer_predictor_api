def violin_plot(tournament, team, position, name, attributum):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import highlight_text
    import matplotlib.font_manager
    from io import BytesIO
    import base64
    import os
    from transferPredict.settings import BASE_DIR

    file_path = os.path.join(BASE_DIR, 'transferPredictApp/who_scored.csv')
    df = pd.read_csv(file_path)

    try:
        player_value = df[(df.Tournament == tournament)&(df.Team == team)&(df.Position == position)\
            &(df.Name == name)][attributum].values[0]
    except:
        player_value = 0

    other_players = df[(df.Tournament == tournament)&(df.Position == position)][attributum].values

    background = "#444444"
    text_color = 'w'
    primary='red'
    mpl.rcParams['xtick.color'] = text_color
    mpl.rcParams['ytick.color'] = text_color
    title_font = 'Perpetua'
    body_font = 'Open Sans'

    player = name
    fig, ax = plt.subplots(figsize=(6,4))

    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)

    ax.grid(ls='dotted', lw='0.5', color='lightgray', zorder= 1)

    parts = ax.violinplot(
            other_players, showmedians=True, quantiles=[0.25, 0.75], vert=False)

    for pc in parts['bodies']:
        pc.set_facecolor('grey')
        pc.set_edgecolor(background)
        pc.set_alpha(0.5)

    parts['cbars'].set_color('w')
    parts['cmins'].set_color('w')
    parts['cmaxes'].set_color('w')
    parts['cmedians'].set_color('w')
    parts['cmedians'].set_linewidth(4)
    parts['cquantiles'].set_color('w')
    parts['cquantiles'].set_linestyles('--')

    highlight_textprops =\
    [{"color": primary, "fontsize":12, "fontfamily":title_font, "fontweight":'bold'},
    {"color": text_color, "fontsize":12, "fontfamily":title_font, "fontweight":'bold'},
    {"color": text_color, "fontsize":10, "fontfamily":body_font}]

    highlight_text.fig_text(x=0.02, y=0.99,
                s=f"<{name}'s> <{attributum.lower()} per game>\n<{tournament} - 2019/2020>\n",
                highlight_textprops=highlight_textprops)

    ax.tick_params(axis="x", labelsize=10)

    ax.set_yticklabels(["Frequency"], color=text_color)
    ax.tick_params(axis='y', labelrotation = 90)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(text_color)
    ax.spines['left'].set_color(text_color)

    ax.plot(player_value, 1, marker="o", markersize=20, markeredgecolor=primary, markerfacecolor=primary)

    violin_fig_path = os.path.join(BASE_DIR, 'transferPredictApp/violin_plot.png')
    plt.savefig(violin_fig_path, format='png')
    with open(violin_fig_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string.decode("utf-8")


