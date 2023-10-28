import streamlit as st
import time

st.title("Jesus")
start_button = st.button("Iniciar/Reiniciar Atualização")

if start_button:
    counter = 0
    while counter < 5:
        st.write("Jesus")
        time.sleep(1)
        counter += 1
        if counter == 10:
            st.empty()  # Limpar a saída após as 10 repetições





