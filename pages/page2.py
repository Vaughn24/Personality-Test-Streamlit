import streamlit as st
import datetime
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page
import re
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

def email_valid(email):
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

def correction():
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    remove_sidebar()
    st.title('Personal Information')
    # Load the existing Excel file
    excel_file_path = "user_answers.xlsx"
    sheet_name = "Sheet1"
    existing_data = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    df_gender = existing_data.loc[0,'Gender']

    # This is for the default value in radio button Gender
    g_index = 0 if df_gender == "Male" else 1 if df_gender == "Female" else 0

    df_birth_date = existing_data.loc[0,'Birth Date']
    if (df_birth_date == " "):
        bd_value = datetime.datetime.now()
    else:
        bd_value = df_birth_date

    first_name = st.text_input("First Name",value=existing_data.loc[0,'First Name'])
    first_name_wmessage = "Please enter your First Name"
    st.markdown(
        f'<div class="fn_wmessage" style="color: red; font-size: 14px; display: none; background-color: 53, 100, 95, 0.7; color: '
        f'#Ff8282; padding: 10px; border-radius: 5px;">{first_name_wmessage}</div>',
        unsafe_allow_html=True
    )

    last_name = st.text_input("Last Name",value=existing_data.loc[0,'Last Name'])
    last_name_wmessage = "Please enter your Last Name"
    st.markdown(
        f'<div class="ln_wmessage" style="color: red; font-size: 14px; display: none; background-color: 53, 100, 95, 0.7; color: '
        f'#Ff8282; padding: 10px; border-radius: 5px;">{last_name_wmessage}</div>',
        unsafe_allow_html=True
    )
    birth_date = st.date_input("Birth Date", min_value=datetime.date(1950,1,1), max_value=datetime.date(2024,1,1),value=bd_value)
    gender = st.radio("Gender", ["Male", "Female", "Prefer not to say"], horizontal=True,index=g_index)
    #email = st.text_input("Email Address",value=existing_data.loc[0,'Email Address'])

    email_default_value = " "
    if existing_data.loc[0,'Email Address'] == " ":
        email_default_value = ""
    else:
        email_default_value = existing_data.loc[0,'Email Address']

    email = st.text_input("Email Address",value=email_default_value)
    email_wmessage = "Please enter valid email address"
    st.markdown(
        f'<div class="email_wmessage" style="color: red; font-size: 14px; display: none; background-color: 53, 100, 95, 0.7; color: '
        f'#Ff8282; padding: 10px; border-radius: 5px;">{email_wmessage}</div>',
        unsafe_allow_html=True
    )
    email2_wmessage = "Please enter enter email address"
    st.markdown(
        f'<div class="email2_wmessage" style="color: red; font-size: 14px; display: none; background-color: 53, 100, 95, 0.7; color: '
        f'#Ff8282; padding: 10px; border-radius: 5px;">{email2_wmessage}</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3,col4, col5, col6 = st.columns(6)
    style = """<style>
    .row-widget.stButton {
    margin-top: 2rem}
    </style>"""
    st.markdown(style, unsafe_allow_html=True)
    with col6:
        if st.button("Next Page"):
            if first_name == " " or first_name == "":
                with col1:
                    if st.button("Prev Page"):
                        switch_page("page1")
                st.markdown(
                    """ <style>
                            div.fn_wmessage{
                                display: block !important;
                            }
                        </style>
                        """,
                    unsafe_allow_html=True
                )
                st.stop()

            elif last_name == " " or last_name == "":
                with col1:
                    if st.button("Prev Page"):
                        switch_page("page1")
                    st.markdown(
                        """ <style>
                                div.ln_wmessage{
                                    display: block !important;
                                }
                            </style>
                            """,
                        unsafe_allow_html=True
                    )
                    st.stop()


            elif not birth_date:
                st.warning("Please select your Birth Date")
            elif email == " " or email == "":
                with col1:
                    if st.button("Prev Page"):
                        switch_page("page1")
                    st.markdown(
                        """ <style>
                                div.email2_wmessage{
                                    display: block !important;
                                }
                            </style>
                            """,
                        unsafe_allow_html=True
                    )
                    st.stop()

            elif not email_valid(email):
                with col1:
                    if st.button("Prev Page"):
                        switch_page("page1")
                    st.markdown(
                        """ <style>
                                div.email_wmessage{
                                    display: block !important;
                                }
                            </style>
                            """,
                        unsafe_allow_html=True
                    )
                    st.stop()

            else:
                # Create a DataFrame from the form data
                data = {
                    "First Name": [first_name],
                    "Last Name": [last_name],
                    "Birth Date": [birth_date],
                    "Gender": [gender],
                    "Email Address": [email]
                }
                df = pd.DataFrame(data)

                try:

                    existing_data.loc[0, 'First Name'] = first_name
                    existing_data.loc[0, 'Last Name'] = last_name
                    existing_data.loc[0, 'Birth Date'] = birth_date
                    existing_data.loc[0, 'Gender'] = gender
                    existing_data.loc[0, 'Email Address'] = email
                    existing_data.to_excel(excel_file_path, sheet_name=sheet_name, index=False)
                    st.success("Data successfully stored in the Excel file!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                switch_page("page3")

    with col1:
        if st.button("Prev Page"):
            switch_page("page1")


