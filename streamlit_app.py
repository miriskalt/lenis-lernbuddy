import streamlit as st

st.title("🌱 Leni's Lernpflanze")
st.write(
    "Lass deine Pflanze wachsen, indem du lernst!"
)

if "minutes" not in st.session_state:
    st.session_state.minutes = 0


minutes_added = st.number_input(
    "Wie viele Minuten hast du gelernt?",
    min_value=1,
    max_value=300,
    value=25,
)


if st.button("Ich habe gelernt!"):
    st.session_state.minutes += minutes_added


total = st.session_state.minutes

st.subheader(f"Gesamte Lernzeit: {total} Minuten")





if st.button("Neue Pflanze starten"):
    st.session_state.minutes = 0
    st.rerun()