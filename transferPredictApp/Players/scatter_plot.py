def scatter_plot(tournament, team, position, name, attr1, attr2):
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
        player_attr1 = df[(df.Tournament == tournament)&(df.Team == team)&(df.Position == position)\
            &(df.Name == name)][attr1].values[0]
        player_attr2 = df[(df.Tournament == tournament)&(df.Team == team)&(df.Position == position)\
            &(df.Name == name)][attr2].values[0]
    except:
        attr1 = 0
        attr2 = 0

    other_attr1 = df[(df.Tournament == tournament)&(df.Position == position)][attr1].values
    other_attr2 = df[(df.Tournament == tournament)&(df.Position == position)][attr2].values

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

    ax.set_xlabel(f'{attr1} per game', fontweight='bold', color=text_color, fontfamily=body_font)
    ax.set_ylabel(f'{attr2} per game', fontweight='bold', color=text_color, fontfamily=body_font)

    ax.scatter(other_attr1, other_attr2,
                s=150,
                color='grey',
                alpha=0.5,
                zorder=2)

    highlight_textprops =\
    [{"color": primary, "fontsize":12, "fontfamily":title_font, "fontweight":'bold'},
    {"color": text_color, "fontsize":12, "fontfamily":title_font, "fontweight":'bold'},
    {"color": text_color, "fontsize":10, "fontfamily":body_font}]

    highlight_text.fig_text(x=0.02, y=0.99,
                s=f"<{name}'s> <{attr1.lower()} and {attr2.lower()} per game>\n<{tournament} - 2019/2020>\n",
                highlight_textprops=highlight_textprops)

    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis='y', labelrotation = 90)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(text_color)
    ax.spines['left'].set_color(text_color)

    ax.plot(player_attr1, player_attr2, marker="o", markersize=20, markeredgecolor=primary, markerfacecolor=primary)

    scatter_fig_path = os.path.join(BASE_DIR, 'transferPredictApp/scatter_plot.png')
    plt.savefig(scatter_fig_path, format='png')
    with open(scatter_fig_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string.decode("utf-8")


