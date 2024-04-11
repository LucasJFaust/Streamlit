import streamlit  as st
import pandas as pd
import numpy as np
import altair as alt

st.write("Este é um texto")

st.write(pd.DataFrame ({
    'Coluna A': [1,2,3,4,5],
    'Coluna B': ["Cachorro", "Gato", "Cavalo", "Vaca", "Zebra"],
}))

array = [1, 2, "abc", "Martin", True]
st.write('Aqui temos uma array', array)