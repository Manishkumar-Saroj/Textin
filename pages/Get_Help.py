import streamlit as st


#--------------------------------SET PAGE CONFIGRATION---------------------------- 
st.set_page_config(
    page_title="Textin",
    layout="wide",   
    initial_sidebar_state="auto",
    
)


#--------------------------------------CODE FOR TO HIDE MAINMENU AND FOOTER----------------------------
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.streamlit-header {background-color: transparent;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Container for the top section to insert logo and basic detail about website
top_container = st.container()

# Two columns within the container
col1, col2 = top_container.columns([3, 1])


col1.header('Hello, 👋')
col1.header('Welcome to the Textin Get Help Section.')
col1.subheader('Here you can see how the Textin website works.')
# Image is for logo of the website.
col2.image('images\logo.png', use_column_width=True) 
st.write('---')

st.write('---')
st.write("""
Sure, here's a more detailed description of how the application works:

1. Registration: The user can register with a unique username, password, and mobile number. This information is stored in a database for future use.

2. Login: The user can log in to the system using their username and password. The system verifies the user's credentials and allows them to proceed to the main page.

3. Reset password and username: If the user forgets their password or username, they can reset it using their mobile number. The system will verify the mobile number and allow the user to set a new password or username.

4. Main page: After successful login, the user is directed to the main page. The main page has three tabs: Audio/Video to Text, My Transcription, and Feedback.

5. Audio/Video to Text: In this tab, the user can select the language of the audio or video file they want to transcribe. Then, they can upload the file to the system, and the transcription process starts automatically. Once the transcription is complete, the user can view the output text and download it in TXT or DOCX format. The output text is also saved in the database for future use.

6. My Transcription: In this tab, the user can see a list of all the text files that they have previously transcribed. If there are no files, the system will show a message that says "No transcripted file available." If there are files, the user can select a file and view its details, including the language, and the text file itself. The user can edit, update, delete, or download the file as TXT or DOCX format. The changes made to the text files are automatically saved in the database.

7. Feedback: In this tab, the user can provide feedback about the application. They can submit their feedback and the system will store it in the database for future reference.

That's a high-level overview of how the application works. Let me know if you have any more questions or need more clarification!
""")