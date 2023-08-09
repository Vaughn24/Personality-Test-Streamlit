import streamlit as st
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

if __name__ == '__main__':
    remove_sidebar()
    st.title('Thank you for your participation')
    style = """<style>
    .row-widget.stButton {
    text-align: left;}
    </style>"""
    st.markdown(style, unsafe_allow_html=True)
    if st.button("Do want to add new response?"):
        switch_page('app')