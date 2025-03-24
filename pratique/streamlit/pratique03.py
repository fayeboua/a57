import streamlit as st
import os

st.title('Pratique 03 - Input Widgets')

# Button
st.header('Button')
button = st.button('Button')  # return True or False
if button:
    st.write('You pressed the Button')

# Checkbox (Toggle Button)
st.header('Checkbox')
checkbox = st.checkbox("Do you want to agree?")  # return bool (True or False)
if checkbox:
    st.write('You checked the box')
else:
    st.write('You unchecked the box')

st.header('Radio Button')
# Radio Button
options = ("India", "USA", "UK", "Australia")
radio_button = st.radio("What is your favorite country", options, index=2)  # return an element in a list/tuple
st.write('Your favorite country is', radio_button)

# Select Box
st.header('Select Box')
options = ('Email', 'Phone', 'WhatsApp')
select_box = st.selectbox('How would you like to contact', options, index=1)
st.write('Your preferred mode of communication is', select_box)

# Slider
st.header('Slider')
slider_range = st.slider('How old are you?', min_value=1, max_value=100, step=1, value=20)
st.write('Your age is', slider_range)

# Text Inputs
st.header('Text Inputs')
name = st.text_input('Enter your Name')
st.write('Your name is', name)

age = st.number_input('Enter your age', min_value=1, max_value=100, step=1, value=25)
st.write('Your age is', age)

# Upload File
st.header('File Upload')
uploaded_file = st.file_uploader('Choose a File')

if uploaded_file is not None:
    st.success('File uploaded successfully')
    details = {'filename': uploaded_file.name, 'filetype': uploaded_file.type, 'filesize (bytes)': uploaded_file.size}
    st.json(details)
    
    # save the file
    path = os.path.join('./upload', uploaded_file.name)
    with open(path, mode='wb') as f:
        f.write(uploaded_file.getbuffer())
        st.success('File saved successfully')