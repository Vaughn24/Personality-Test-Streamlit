import streamlit as st
import pandas as pd
import csv
from itertools import chain
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

if __name__ == '__main__':
    remove_sidebar()
    st.title('Physiognomy Personality Test Results')
    excel_file_path = "user_answers.xlsx"
    sheet_name = "Sheet1"
    df = pd.read_excel(excel_file_path)
    df3 = df.copy()

    favorable = [2, 3, 4, 5, 7, 8, 11, 14, 17, 18, 22, 23, 24, 26, 27, 28, 30, 31, 32, 33, 34, 37, 39, 40, 43, 45, 46,
                 47, 48, 49, 53, 57, 58, 60, 61, 62, 64, 65, 67, 68, 69, 71, 73, 78, 81, 83, 86, 88, 97, 98]
    unfavorable = [1, 6, 9, 10, 12, 13, 15, 16, 19, 20, 21, 25, 29, 35, 36, 38, 41, 42, 44, 50, 51, 52, 54, 55, 56, 59,
                   63, 66, 70, 72, 74, 75, 76, 77, 79, 80, 82, 84, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 99, 100]

    row_index = 0
    values_list = df3.iloc[row_index].tolist()

    rating = values_list[6::]
    questionnaire_score = {key: value for key, value in enumerate(rating, 1)}

    # For checking
    questionnaire_score_not_scaled = {key: value for key, value in enumerate(rating, 1)}


    value_mapping = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
    unfavorable_scores = [value_mapping[questionnaire_score[key]] for key in unfavorable if key in questionnaire_score]
    questionnaire_score.update(zip(unfavorable, unfavorable_scores))

    # Honesty-Humilty
    Sincerity = [questionnaire_score[key] for key in [6, 30, 54, 78] if key in questionnaire_score]
    Fairness = [questionnaire_score[key] for key in [12, 36, 60, 84] if key in questionnaire_score]
    Greed_Avoidance = [questionnaire_score[key] for key in [18, 42, 66, 90] if key in questionnaire_score]
    Modesty = [questionnaire_score[key] for key in [24, 48, 72, 96] if key in questionnaire_score]

    # Grand Total Honest-Humilty
    combined_list = chain(Sincerity, Fairness, Greed_Avoidance, Modesty)
    GT_Honesty_Humility = sum(combined_list)

    Fearfulness = [questionnaire_score[key] for key in [5, 29, 53, 77] if key in questionnaire_score]
    Anxiety = [questionnaire_score[key] for key in [11, 35, 59, 83] if key in questionnaire_score]
    Dependence = [questionnaire_score[key] for key in [17, 41, 65, 89] if key in questionnaire_score]
    Sentimentality = [questionnaire_score[key] for key in [23, 47, 71, 95] if key in questionnaire_score]

    # Grand Total Emotionality
    combined_list2 = chain(Fearfulness, Anxiety, Dependence, Sentimentality)
    GT_Emotionality = sum(combined_list2)

    # Extraversion
    Social_SE = [questionnaire_score[key] for key in [4, 28, 52, 76] if key in questionnaire_score]
    Social_Boldness = [questionnaire_score[key] for key in [10, 34, 58, 82] if key in questionnaire_score]
    Sociability = [questionnaire_score[key] for key in [16, 40, 64, 88] if key in questionnaire_score]
    Liveliness = [questionnaire_score[key] for key in [22, 46, 70, 94] if key in questionnaire_score]

    # Grand Total Extraversion
    combined_list3 = chain(Social_SE, Social_Boldness, Sociability, Liveliness)
    GT_Extraversion = sum(combined_list3)

    # Agreeableness

    Forgiveness = [questionnaire_score[key] for key in [3, 27, 51, 75] if key in questionnaire_score]
    Gentleness = [questionnaire_score[key] for key in [9, 33, 57, 81] if key in questionnaire_score]
    Flexibility = [questionnaire_score[key] for key in [15, 39, 63, 87] if key in questionnaire_score]
    Patience = [questionnaire_score[key] for key in [21, 45, 69, 93] if key in questionnaire_score]

    # Grand Total Agreeableness
    combined_list4 = chain(Forgiveness, Gentleness, Flexibility, Patience)
    GT_Agreeableness = sum(combined_list4)

    # Conscientiousness

    Organization = [questionnaire_score[key] for key in [2, 26, 50, 74] if key in questionnaire_score]
    Diligence = [questionnaire_score[key] for key in [8, 32, 56, 80] if key in questionnaire_score]
    Perfectionism = [questionnaire_score[key] for key in [14, 38, 62, 86] if key in questionnaire_score]
    Prudence = [questionnaire_score[key] for key in [20, 44, 68, 92] if key in questionnaire_score]

    # Grand Total Conscientiousness
    combined_list5 = chain(Organization, Diligence, Perfectionism, Prudence)
    GT_Conscientiousness = sum(combined_list5)

    # Openness to Experience

    Aesth_App = [questionnaire_score[key] for key in [1, 25, 49, 73] if key in questionnaire_score]
    Inquisitiveness = [questionnaire_score[key] for key in [7, 31, 55, 79] if key in questionnaire_score]
    Creativity = [questionnaire_score[key] for key in [13, 37, 61, 85] if key in questionnaire_score]
    Unconventionality = [questionnaire_score[key] for key in [19, 43, 67, 91] if key in questionnaire_score]

    # Grand Total Conscientiousness
    combined_list6 = chain(Aesth_App, Inquisitiveness, Creativity, Unconventionality)
    GT_OtoE = sum(combined_list6)

    # Altruism
    Altruism = [questionnaire_score[key] for key in [97, 98, 99, 100] if key in questionnaire_score]
    GT_altruism = sum(Altruism)
    alt_rating = "HIGH" if GT_altruism >= 15 else ("LOW " if GT_altruism < 9 else "MID ")

    # Get the Grand total of each Factor and Facet
    score_FnF = [Sincerity, Fairness, Greed_Avoidance, Modesty, Fearfulness, Anxiety, Dependence, Sentimentality,
                 Social_SE, Social_Boldness, Sociability, Liveliness, Forgiveness, Gentleness, Flexibility, Patience,
                 Organization, Diligence, Perfectionism, Prudence, Aesth_App, Inquisitiveness, Creativity,
                 Unconventionality, Altruism]
    GT_FnF = [sum(inner_list) for inner_list in score_FnF]

    # DESCRIPTION range without the Altruism
    GT_PA = [GT_Honesty_Humility, GT_Emotionality, GT_Extraversion, GT_Agreeableness, GT_Conscientiousness, GT_OtoE]


    # Description range for Personality Aspect
    def description_range_PA(GT):
        rating = ""
        if GT >= 59:
            rating = "HIGH"
        elif GT < 37:
            rating = "LOW "
        else:
            rating = "MID "
        return rating


    # Description range for Factor and Facet
    def description_range_FnF(GT):
        rating = ""
        if GT >= 15:
            rating = "HIGH"
        elif GT < 9:
            rating = "LOW "
        else:
            rating = "MID "
        return rating


    PA_rating = []

    FnF_rating = []
    for PA in GT_PA:
        PA_rating.append(description_range_PA(PA))
    for FnF in GT_FnF:
        FnF_rating.append(description_range_FnF(FnF))

    # Altruism have different formula
    PA_rating.append(alt_rating)
    GT_PA.append(GT_altruism)

    # HEXACO
    PA_sum = sum(GT_PA)
    HEX_rating = "HIGH" if PA_sum >= 367 else ("LOW " if PA_sum < 233 else "MID ")

    Name = df3["First Name"][row_index] + " " + df3["Last Name"][row_index]
    Birth_Date = str(df3["Birth Date"][row_index])
    Gender = df3["Gender"][row_index]
    Email = df3["Email Address"][row_index]

    df_PA_column = ['PERSONALITY ASPECTS', 'RATING', 'TOTAL SCORE']
    df_FnF_column = ['FACTORY AND FACET', 'RATING', 'TOTAL SCORE']
    personality_aspect = txt_to_list('asset/Personality-Aspects.txt')
    factory_and_facet = txt_to_list('asset/Factor-and-Facet.txt')

    PA_data = {
        df_PA_column[0]: personality_aspect,
        df_PA_column[1]:  PA_rating,
        df_PA_column[2]: GT_PA
    }
    df_PA_results = pd.DataFrame(PA_data)

    FnF_data = {
        df_FnF_column[0]: factory_and_facet,
        df_FnF_column[1]:  FnF_rating,
        df_FnF_column[2]: GT_FnF
    }
    df_FnF_results = pd.DataFrame(FnF_data)

    df_Hex_column = ['PERSONALITY TEST', 'RATING', 'TOTAL SCORE']
    Hex_data = {
        df_Hex_column[0]: ['HEXACO'],
        df_Hex_column[1]:  HEX_rating,
        df_Hex_column[2]: PA_sum
    }
    df_Hex_results = pd.DataFrame(Hex_data)

    st.markdown(
        f"""
    <span style='background-color: none;'>Name:</span>
    <span style='font-size: Large;'>{Name}</span>
    
    <span style='background-color: none;'>Birth Date:</span>
    <span style='font-size: Large;'>{Birth_Date[:10]}</span>

    <span style='background-color: none;'>Gender:</span>
    <span style='font-size: Large;'>{Gender}</span>

    <span style='background-color: none;'>Email:</span>
    <span style='font-size: Large;'>{Email}</span>

""",
        unsafe_allow_html=True)


    df_PA_results
    df_FnF_results
    df_Hex_results


    ########## For Checking ######################

    style = """<style>
    .row-widget.stButton {
    text-align: right;}
    </style>"""
    st.markdown(style, unsafe_allow_html=True)
    if st.button("Finish"):
        switch_page('page6')
    elif st.button("Checking Button"):
        favorable_scores = [questionnaire_score_not_scaled[key] for key in favorable if
                            key in questionnaire_score_not_scaled]
        unfavorable_scores = [questionnaire_score_not_scaled[key] for key in unfavorable if
                              key in questionnaire_score_not_scaled]

        output_file = 'checking.csv'

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Favorable', 'Rating', 'Unfavorable', 'Rating'])  # Write header if needed
            for i, j in zip(favorable, unfavorable):
                writer.writerow([i, questionnaire_score_not_scaled[i], j, questionnaire_score_not_scaled[j]])
        csvfile.close()
    elif st.button("Save to database"):
        excel_file_path = "user_answers.xlsx"
        sheet_name = "Sheet1"
        existing_data = pd.read_excel(excel_file_path, sheet_name=sheet_name)



        print(df_PA_results["RATING"][0])

















