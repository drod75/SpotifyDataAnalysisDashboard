import streamlit as st
import pandas as pd
from app.data import get_data, distinct_genres, distinct_types

# session state
get_data()
if "genres" not in st.session_state:
    st.session_state['genres'] = distinct_genres(st.session_state['df'])

if "types" not in st.session_state:
    st.session_state['types'] = distinct_types(st.session_state['df'])

@st.cache_data()
def data_copy():
    return st.session_state["df"].copy()


df_to_process: pd.DataFrame = data_copy()

# sidebar
with st.sidebar:
    st.session_state["genres_selected"] = st.multiselect(
        ":green[What music genres would you like!]", st.session_state["genres"]
    )

    st.session_state["types_selected"] = st.multiselect(
        ":green[What release types do you want to see?]", st.session_state["types"]
    )


# main content
st.header(":green[Spotify Dashboard]", divider="green")


if st.session_state["genres_selected"]:
    genres_string: str = "|".join(st.session_state["genres_selected"])
    df_to_process = df_to_process[
        df_to_process["artist_genres"].str.contains(genres_string)
    ]

if st.session_state["types_selected"]:
    df_to_process = df_to_process[
        df_to_process["album_type"].isin(st.session_state["types_selected"])
    ]

with st.expander("Spotify Dataframe", icon=":material/dataset:"):
    st.dataframe(df_to_process, hide_index=True)
