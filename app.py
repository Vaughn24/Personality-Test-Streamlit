import streamlit as st

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

    likert_options = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']

    # Initialize a dictionary to store user responses
    responses = {}

    # Loop through the questions and display them with a Likert scale widget
    for idx, question in enumerate(questions):
        st.subheader(f'Q{idx + 1}: {question}')
        response = st.selectbox(' ', likert_options, key=f'likert_{idx}')
        responses[f'Q{idx + 1}'] = response

    st.write('\n\n---\n\n')
    st.subheader('Survey Summary')

    # Display the user responses in a table
    response_table = [(question, responses[question]) for question in responses]
    st.table(response_table)



if __name__ == '__main__':
    #
    questions_list = txt_to_list('asset/list-of-questions.txt')
    #print(result_list)
    likert_scale_survey(questions_list)