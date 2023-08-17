import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from openpyxl import load_workbook


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

def txt_to_list(txt_file_path):
    """
    This function turn text file into list
    :param txt_file_path: This should be the text file that you want to turn in to a list
    :return: list
    """
    with open(txt_file_path, 'r') as txt_file:
        data_list = txt_file.read().splitlines()
    return data_list


if __name__ == '__main__':
    remove_sidebar()
    st.title('Physiognomy Personality Test')
    questions = txt_to_list('asset/list-of-questions.txt')
    # Questions and corresponding Likert scale options
    likert_options = ['','Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']
    # Initialize a dictionary to store user responses
    responses = {}
    # Loop through the questions and display them with a Likert scale widget
    for idx, question in enumerate(questions):
        if idx == 0 or responses.get(f'Q{idx}'):
            st.subheader(f'Q{idx + 1}: {question}')
            key = f'question_{idx}'
            #placeholder = st.empty()
            st.markdown(
                """ <style>
                        div[role="radiogroup"] >  :first-child{
                            display: none !important;
                        }
                    </style>
                    """,
                unsafe_allow_html=True
            )
            response = st.radio(' ', likert_options, key=key, horizontal=True, index=0)
            responses[f'Q{idx + 1}'] = response
            #placeholder.empty()

    st.write('\n\n---\n\n')
    #st.subheader('Survey Summary')

    # Display the user responses in dataframe panda
    response_table = [(f'Q{idx+1}', responses[question], likert_options.index(responses[question])) for idx, question in enumerate(responses)]
    df_response_table = pd.DataFrame(response_table, columns=['Question', 'Response', 'Response Index'])


    #st.dataframe(df_response_table)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    excel_file_path = "user_answers.xlsx"
    sheet_name = "Sheet1"
    existing_data = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    with col6:
        if st.button("Next Page"):
            nan_check = (df_response_table['Response Index'] == 0).any()
            if nan_check:
                if st.button("Prev Page"):
                    switch_page("page2")
                st.error("Please answer all the questions.")
            else:
                questions_no_list = df_response_table['Question']
                response_index_list = df_response_table['Response Index']
                for col_name, col_values in zip(questions_no_list, response_index_list):
                    existing_data.loc[0, col_name] = col_values
                    existing_data.to_excel(excel_file_path, sheet_name=sheet_name, index=False)
                try:
                    st.success("Data successfully stored in the Excel file!")
                    switch_page("page4")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    with col1:
        if st.button("Prev Page"):
            switch_page("page2")

