import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px


def pca_plot(file):
    df = pd.read_csv(file)
    X = df[['danceability', "energy", "key", 'loudness', 'mode',
             'speechiness', 'acousticness', 'instrumentalness',
             'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']]

    pca = PCA(n_components=2)
    components = pca.fit_transform(X)

    fig = px.scatter(components, x=0, y=1, color=df['multiclass_label'])
    fig.show()


if __name__ == '__main__':
    file = 'data/all_data.csv'
    pca_plot(file)

