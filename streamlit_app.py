import streamlit as st

st.title("🌱 Leni's Lernpflanze")
st.write(
    "Lass deine Pflanze wachsen, indem du lernst!"
)


minutes_added = st.number_input(
    "Wie viele Minuten hast du gelernt?",
    min_value=1,
    max_value=300,
    value=25,
)
