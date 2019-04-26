import urllib.request
import os
import pandas as pd
import postgresql as psql


def dropbox_down(url, file_name):

    u = urllib.request.urlopen(url)
    data = u.read()
    u.close()

    with open(file_name, "wb") as f:
        f.write(data)


def unzip(file_path):
    os.system('gunzip ' + file_path)


title_url = "https://www.dropbox.com/s/3do9bu0awq048uh/title.basics.tsv.gz?dl=1"
name_url = "https://www.dropbox.com/s/xaidig3yw2viyym/name.basics.tsv.gz?dl=1"

dropbox_down(title_url, "title.basics.tsv.gz")
dropbox_down(name_url, "name.basics.tsv.gz")

unzip("title.basics.tsv.gz")
unzip("name.basics.tsv.gz")


def load_movie_data(file_name, row_limit):
    df = pd.read_csv(file_name, sep='\t', header=0, nrows=row_limit)
    df['endYear'] = df['endYear'].apply(
        lambda x: x if isinstance(x, int) else 0)
    df['runtimeMinutes'] = df['runtimeMinutes'].apply(
        lambda x: x if isinstance(x, int) else 0)
    df['originalTitle'] = df['originalTitle'].apply(
        lambda x: str(x).replace('\'', ''))
    df['primaryTitle'] = df['primaryTitle'].apply(
        lambda x: str(x).replace('\'', ''))
    return df


def load_actor_data(file_name, row_limit):
    df = pd.read_csv(file_name, sep='\t', header=0, nrows=row_limit)
    df['deathYear'] = df['deathYear'].apply(
        lambda x: x if isinstance(x, int) else 0)
    df['birthYear'] = df['birthYear'].apply(
        lambda x: x if isinstance(x, int) else 0)
    df['primaryName'] = df['primaryName'].apply(
        lambda x: str(x).replace('\'', ''))
    return df


def load_assoc_data(file_name, row_limit):
    df = pd.read_csv(file_name, sep='\t', header=0, nrows=row_limit)
    df = df[['nconst', 'knownForTitles']]
    df = df.set_index('nconst') \
        .knownForTitles.str.split(',', expand=True) \
        .stack() \
        .reset_index('nconst') \
        .rename(columns={0: 'knownForTitles'}) \
        .reset_index(drop=True)
    return df


def insert_df(connection, df, table_name):
    cursor = connection.cursor()
    for i in range(len(df)):
        row = str(tuple(df.iloc[i]))
        try:
            cursor.execute("INSERT INTO " + table_name + " VALUES {} ".format(row))
        except:
            connection.rollback()


def insert_df2(connection, df, table_name):
    cursor = connection.cursor()
    for i in range(len(df)):
        row = str(tuple(df.iloc[i]))
        try:
            cursor.execute("INSERT INTO " + table_name + "(actor_id_id, movie_id_id) VALUES {} ".format(row))
            connection.commit()
        except:
            connection.rollback()


movie_df = load_movie_data('title.basics.tsv', 10000)
actor_df = load_actor_data('name.basics.tsv', 10000)
assoc_df = load_assoc_data('name.basics.tsv', 9999999)

connection = psql.connect()

insert_df(connection, actor_df, '"IMDB_actor"')
insert_df(connection, movie_df, '"IMDB_movie"')

insert_df2(connection, assoc_df, '"IMDB_movieactorassoc"')


