import streamlit as st
def likert_scale_survey():
    st.title('Likert Scale Survey')

    # Questions and corresponding Likert scale options
    questions = [
        'The product was easy to use.',
        'The product met my expectations.',
        'I would recommend the product to others.',
        'Overall, I am satisfied with the product.'
    ]
    likert_options = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']

    # Initialize a dictionary to store user responses
    responses = {}

    # Loop through the questions and display them with a Likert scale widget
    for idx, question in enumerate(questions):
        st.subheader(f'Q{idx + 1}: {question}')
        response = st.selectbox('', likert_options, key=f'likert_{idx}')
        responses[f'Q{idx + 1}'] = response

    st.write('\n\n---\n\n')
    st.subheader('Survey Summary')

    # Display the user responses in a table
    response_table = [(question, responses[question]) for question in responses]
    st.table(response_table)

if __name__ == '__main__':
    likert_scale_survey()