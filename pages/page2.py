import streamlit as st
import datetime
import pandas as pd
import numpy as np
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
    st.title('Personal Information')
    style = """<style>
    .row-widget.stButton {
    text-align: right;}
    </style>"""
    st.markdown(style, unsafe_allow_html=True)


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
    last_name = st.text_input("Last Name",value=existing_data.loc[0,'Last Name'])
    birth_date = st.date_input("Birth Date", min_value=datetime.date(1950,1,1), max_value=datetime.date(2024,1,1),value=bd_value)
    gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True,index=g_index)
    email = st.text_input("Email Address",value=existing_data.loc[0,'Email Address'])

    if st.button("Next Page"):
        if not first_name:
            st.warning("Please enter your First Name")
        elif not last_name:
            st.warning("Please enter your Last Name")
        elif not birth_date:
            st.warning("Please select your Birth Date")
        elif not gender:
            st.warning("Please select your Gender")
        elif not email:
            st.warning("Please enter your Email Address")
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

                existing_data.loc[0,'First Name'] = first_name
                existing_data.loc[0, 'Last Name'] = last_name
                existing_data.loc[0, 'Birth Date'] = birth_date
                existing_data.loc[0, 'Gender'] = gender
                existing_data.loc[0, 'Email Address'] = email
                existing_data.to_excel(excel_file_path, sheet_name=sheet_name, index=False)
                st.success("Data successfully stored in the Excel file!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
            switch_page("page3")
    elif st.button("Prev Page"):
        switch_page("page1")

