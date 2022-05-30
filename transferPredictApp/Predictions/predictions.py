def predictions(tournament, team, position):
    import pandas as pd
    import os
    from transferPredict.settings import BASE_DIR

    if tournament == 'LaLiga':
        df_metrics = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/df_metrics_SP.csv'))
        feature_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/feature_df_SP.csv'))
        result_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/result_SP.csv'))
    elif tournament == 'Premier League':
        df_metrics = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/df_metrics_EN.csv'))
        feature_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/feature_df_EN.csv'))
        result_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/result_EN.csv'))
    elif tournament == 'Serie A':
        df_metrics = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/df_metrics_IT.csv'))
        feature_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/feature_df_IT.csv'))
        result_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/result_IT.csv'))
    elif tournament == 'Bundesliga':
        df_metrics = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/df_metrics_GE.csv'))
        feature_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/feature_df_GE.csv'))
        result_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/result_GE.csv'))
    else:
        df_metrics = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/df_metrics_FR.csv'))
        feature_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/feature_df_FR.csv'))
        result_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/result_FR.csv'))

    df_metrics = df_metrics.drop('Unnamed: 0', axis=1)
    feature_df = feature_df.round(2)
    result_df = result_df.drop(['Unnamed: 0', 'ID'], axis=1)
    result_df = result_df.round(2)
    result_df = result_df[result_df.Position == position].iloc[:50]
    result_df = result_df.sort_values(by='Probability', ascending=False)

    return (df_metrics.to_dict('records'), feature_df.to_dict('records'), result_df.to_dict('records'))