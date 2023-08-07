import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


def remove_sidebar():

    st.set_page_config(initial_sidebar_state="collapsed")
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

def next_button():
    style = """<style>
    .row-widget.stButton {
    text-align: right;}
    </style>"""
    st.markdown(style, unsafe_allow_html=True)
    if st.button("Next Page"):
        switch_page("page1")
    #st.markdown('<a href="/page1" target="_self">Next page</a>', unsafe_allow_html=True)


if __name__ == '__main__':
    remove_sidebar()
    st.title('Physiognomy Personality Test')
    next_button()

    #print(df_survey_responses)
