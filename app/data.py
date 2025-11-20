import streamlit as st
import pandas as pd
import duckdb

def get_data(file_path: str = "data/spotify_2025_data.csv"):
    try:
        con = duckdb.connect(":memory:")
        df = con.sql(f"""
            SELECT 
                * REPLACE(trim(lower(artist_genres)) AS artist_genres)
            FROM '{file_path}'
        """).df()
        
        st.session_state["df"] = df

    except Exception as E:
        raise Exception(f"Error connecting to data! {E}")

def distinct_genres(df: pd.DataFrame) -> list[str]:
    try:
        query = """
            SELECT DISTINCT trim(genre) 
            FROM (
                SELECT unnest(string_split(artist_genres, ',')) as genre 
                FROM df
            ) 
            WHERE genre IS NOT NULL AND genre != ''
            ORDER BY 1 ASC
        """
        return [x[0] for x in duckdb.sql(query).fetchall()]
        
    except Exception as E:
        raise Exception(f"Error getting unique artist genres via DuckDB! {E}")

def distinct_types(df: pd.DataFrame) -> list[str]:
    try:
        query = """
            SELECT DISTINCT album_type 
            FROM df 
            ORDER BY album_type ASC
        """
        return [x[0] for x in duckdb.sql(query).fetchall()]
        
    except Exception as E:
        raise Exception(f"Error getting unique album types via DuckDB! {E}")
