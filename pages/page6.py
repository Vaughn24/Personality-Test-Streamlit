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
    st.write("""
 
    We genuinely appreciate your completion of the test, as they are incredibly valuable in helping us understand the subject better. 
    Please rest assured that the information you've shared will be kept confidential and will not be shared publicly. 
    We will only use your responses for analysis and to make improvements where necessary.
    """)