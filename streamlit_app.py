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



if total < 30:
    plant = "🌱"
    stage = "Keimling"
elif total < 60:
    plant = "🌿"
    stage = "Junge Pflanze"
elif total < 120:
    plant = "🪴"
    stage = "Kräftig am Wachsen"
elif total < 300:
    plant = "🌷"
    stage = "Blühende Pflanze"
else:
    plant = "🌳"
    stage = "Lernbaum"


st.markdown(
    f"""
    <div style="text-align:center;font-size:120px;">
        {plant}
    </div>
    """,
    unsafe_allow_html=True,
)

st.success(f"Stufe: {stage}")


if st.button("Neue Pflanze starten"):
    st.session_state.minutes = 0
    st.rerun()