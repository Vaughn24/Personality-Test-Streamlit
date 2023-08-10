import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os
import pandas as pd
from PIL import Image
import datetime

def load_image(image_file):
    img = Image.open(image_file)
    return img
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
    st.markdown(style, unsafe_allow_html=True)

    image_file = st.file_uploader("Upload An Image", type=['png', 'jpeg', 'jpg'])
    if image_file is not None:
        file_details = {"FileName": image_file.name, "FileType": image_file.type}
        #st.write(file_details)
        img = load_image(image_file)
        st.image(img)

        df = pd.read_excel("user_answers.xlsx")
        Name = df["First Name"][0] + " " + df["Last Name"][0]
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        image_extension = image_file.name.split('.')[-1].lower()
        image_file_name = str(Name+current_time)+"." + image_extension
        image_file_name = image_file_name.replace(" ","")

        #
        with open(os.path.join("user_img", image_file_name), "wb") as f:
            f.write(image_file.getbuffer())
        st.success("Saved File")

    if st.button("Next Page"):
        excel_file_path = "user_answers.xlsx"
        sheet_name = "Sheet1"
        existing_data = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        #print(existing_data)
        try:
            #existing_data.loc[0:2, "Image Name"] = image_file_name
            existing_data.insert(6,"Image Name",image_file_name)
            existing_data.to_excel(excel_file_path, sheet_name=sheet_name, index=False)
            switch_page("page5")
        except:
            st.write("Please upload an image")

        #switch_page("page5")
    elif st.button("Prev Page"):
        switch_page("page3")

