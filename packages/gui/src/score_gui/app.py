import streamlit as st
from score_core.domain.entities.garment import Garment
from score_core.application.use_cases.recommend_outfit import recommend_outfits

st.title("SCORE Demo (Stub)")

context = st.selectbox("Context", ["university", "university-elegant", "presentation", "gym", "party"])
top = st.selectbox("Top color", ["black", "white", "orange", "red", "blue", "green"])
bottom = st.selectbox("Bottom color", ["black", "white", "green", "blue", "beige"])

if st.button("Recommend"):
    current = [Garment(kind="top", color_primary=top), Garment(kind="bottom", color_primary=bottom)]
    recs = recommend_outfits(current=current, context=context)
    for r in recs:
        st.write(f"Score: {r.score}")
        st.write(r.explanation)
