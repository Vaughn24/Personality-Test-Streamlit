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

if __name__ == '__main__':
    remove_sidebar()
    st.title('Physiognomy Personality Test')
    style = """<style>
    .row-widget.stButton {
    text-align: right;}
    </style>"""
    st.markdown(style, unsafe_allow_html=True)
    entrycode = st.text_input("Enter Survey Code")
    entrycode_wmessage = "Code has been already been used."
    entrycode_wmessage2 = "Invalid Code."
    st.markdown(
        f'<div class="entrycode_wmessage" style="color: red; font-size: 14px; display: none; background-color: 53, 100, 95, 0.7; color: '
        f'#Ff8282; padding: 10px; border-radius: 5px;">{entrycode_wmessage}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="entrycode_wmessage2" style="color: red; font-size: 14px; display: none; background-color: 53, 100, 95, 0.7; color: '
        f'#Ff8282; padding: 10px; border-radius: 5px;">{entrycode_wmessage2}</div>',
        unsafe_allow_html=True
    )
    entrycode_df = pd.read_excel("entrycode.xlsx", sheet_name="Sheet1")
    if st.button("Next Page"):
        for idx in range(len(entrycode_df)-1):
            if entrycode_df["code"][idx] == entrycode:
                if entrycode_df["used"][idx] == 0:
                    entrycode_df.loc[idx, 'used'] = 1
                    entrycode_df.to_excel("entrycode.xlsx", sheet_name="Sheet1", index=False)
                    switch_page("page1")
                else:
                    st.markdown(
                        """ <style>
                                div.entrycode_wmessage{
                                    display: block !important;
                                }
                            </style>
                            """,
                        unsafe_allow_html=True
                    )
                    break
            if idx == (len(entrycode_df)-2):
                st.markdown(
                    """ <style>
                            div.entrycode_wmessage2{
                                display: block !important;
                            }
                        </style>
                        """,
                    unsafe_allow_html=True
                )

    #print(df_survey_responses)
