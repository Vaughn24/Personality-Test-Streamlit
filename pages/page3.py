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
    st.title('Please upload an image')
    style = """<style>
    .row-widget.stButton {
    text-align: right;}
    </style>"""

    file = st.file_uploader("Pick a file.")
    if st.button("Next Page"):
        switch_page("page4")
    elif st.button("Prev Page"):
        switch_page("page2")

