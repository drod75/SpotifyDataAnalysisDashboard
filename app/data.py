import streamlit as st
import pandas as pd
import duckdb


def get_data(file_path: str = "data/spotify_2025_data.csv"):
    try:
        con = duckdb.connect(":memory:")
        df = con.read_csv(file_path).df()
        st.session_state["df"] = df

    except Exception as E:
        raise Exception("Error connecting to data!")


def distinct_genres(df: pd.DataFrame) -> list[str]:
    try:
        genres = df["artist_genres"].str.split(",").explode()
        genre_frame = genres.to_frame()
        genre_frame["artist_genres"] = genre_frame["artist_genres"].str.lower()
        genre_frame["artist_genres"] = genre_frame["artist_genres"].str.strip()
        genres_gb = (
            genre_frame.groupby("artist_genres")["artist_genres"]
            .count()
            .reset_index(name="count")
        )
        genres_gb.sort_values("count", ascending=False, inplace=True)
        genres_gb.reset_index(drop=True, inplace=True)
        unique_genres = genres_gb["artist_genres"].to_list()

        return unique_genres
    except Exception as E:
        raise Exception("Error getting unique artist genres from Pandas Dataframe!")
