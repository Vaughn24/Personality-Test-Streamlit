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

def txt_to_list(txt_file_path):
    """
    This function turn text file into list
    :param txt_file_path: This should be the text file that you want to turn in to a list
    :return: list
    """
    with open(txt_file_path, 'r') as txt_file:
        data_list = txt_file.read().splitlines()
    return data_list

def likert_scale_survey(list_of_questions):
    """
    This function will create a survey form base on the list given questions
    :param list_of_questions: Insert a list of questions
    :return:
    """
    st.title('Likert Scale Survey')

    # Questions and corresponding Likert scale options
    questions = list_of_questions

    likert_options = ['','Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']

    # Initialize a dictionary to store user responses
    responses = {}

    # Loop through the questions and display them with a Likert scale widget
    for idx, question in enumerate(questions):
        if idx == 0 or idx == 1 or responses.get(f'Q{idx}'):
            st.subheader(f'Q{idx + 1}: {question}')
            key = f'question_{idx}'
            placeholder = st.empty()
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
            placeholder.empty()

    st.write('\n\n---\n\n')
    st.subheader('Survey Summary')

    # Display the user responses in dataframe panda
    response_table = [(f'Q{idx+1}', responses[question], likert_options.index(responses[question])) for idx, question in enumerate(responses)]
    df_response_table = pd.DataFrame(response_table, columns=['Question', 'Response', 'Response Index'])
    return df_response_table

def next_button():
    st.markdown('<a href="/page1" target="_self">Next page</a>', unsafe_allow_html=True)


if __name__ == '__main__':
    #
    remove_sidebar()
    questions_list = txt_to_list('asset/list-of-questionsV2.txt')
    df_survey_responses = likert_scale_survey(questions_list)
    st.dataframe(df_survey_responses)
    next_button()
    #switch_page("page1")
    #print(df_survey_responses)
