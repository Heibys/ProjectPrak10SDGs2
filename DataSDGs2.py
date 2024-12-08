import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

df = pd.read_csv('SDGs_Zero_Hunger.csv')

with st.sidebar:
    selected = option_menu(
        'Data Zero Hunger',
        ['SDG Zero Hunger Score', 'Kategori Zero Hunger Negara'],
        default_index=0
    )

if selected == 'SDG Zero Hunger Score':
    st.title("SDGs Zero Hunger")
    st.write("Masukkan nama negara untuk melihat skor:")
    NamaNegara = st.text_input("Nama negara", key="score_input")  # Tambahkan key untuk input

    if NamaNegara:
        data = df[df['NamaNegara'].str.contains(NamaNegara, case=False, na=False)]
        if not data.empty:
            st.dataframe(data)
        else:
            st.warning(f"Data untuk negara **{NamaNegara}** tidak ditemukan.")

if selected == 'Kategori Zero Hunger Negara':
    st.title("SDGs Zero Hunger")
    st.write("Masukkan nama negara untuk mengetahui kategorinya:")
    Kategori = st.text_input("Nama negara", key="kategori_input")  # Tambahkan key untuk input

    if Kategori:
        data1 = df[df['NamaNegara'].str.contains(Kategori, case=False, na=False)]
        if not data1.empty:
            kategori1 = data1.iloc[0]['Kategori']
            st.success(f"Negara **{Kategori}** ini dalam kategori: **{kategori1}**")
        else:
            st.warning(f"Data untuk negara **{Kategori}** tidak ditemukan.")
