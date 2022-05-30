def predictions(tournament, team, position):
    import pandas as pd
    import os
    from transferPredict.settings import BASE_DIR

    file_path = os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/result.csv')
    df_metrics = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/df_metrics.csv'))
    df_metrics = df_metrics.drop('Unnamed: 0', axis=1)
    feature_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/feature_df.csv'))
    feature_df = feature_df.drop('Unnamed: 0', axis=1)
    feature_df = feature_df.round(2)
    result_df = pd.read_csv(os.path.join(BASE_DIR, 'transferPredictApp/Predictions/Data/result.csv'))
    result_df = result_df.drop(['Unnamed: 0', 'ID'], axis=1)
    result_df = result_df.round(2)

    result_df = result_df[result_df.Position == position].iloc[:100]
    result_df = result_df.sort_values(by='Probability', ascending=False)

    return (df_metrics.to_dict('records'), feature_df.to_dict('records'), result_df.to_dict('records'))