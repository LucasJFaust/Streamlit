import streamlit as st

st.title('Esse é o Título')
st.header("Header do ST")
st.subheader("Subheader do ST")

st.markdown("A nota dos alunos foi em **média**, maior que no *semestre* passado")

st.caption("este é o caption")

# code
code = """if(fome>0):
    return "ir para geladeira"
else:
    return "estudar streamlit" """
st.code(code, language = 'python')

st.text('Esse é um texto usando st.text')

# Latex https://katex.org/docs/supported.html

st.latex('\int x²+y²+32ab \isin x²+y²+z²')