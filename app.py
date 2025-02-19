import streamlit as st

def hello_word():
    return  'Minha primeira Dash em Streamlit'

def main():
    st.write(hello_word())

if __name__ == "__main__":
    main()
