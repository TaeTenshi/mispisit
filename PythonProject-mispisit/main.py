import streamlit as st

st.set_page_config(page_title="Anomaly Detector", page_icon="📈")

st.title("Anomaly Detector")
st.subheader("Информационная система обнаружения аномалий в CSV временных рядах")
st.text("Версия 0.0.1")
st.text("Разработка продолжается")

st.divider()
st.caption(
    "Система предназначена для автоматического анализа временных рядов "
    "из CSV-файлов и выявления аномальных участков. "
    "Работает быстрее, чем ручная проверка данных."
)