import streamlit as st


#--------------------------------SET PAGE CONFIGRATION---------------------------- 
st.set_page_config(
    page_title="Textin",
        
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
col1.header('Welcome to the Textin Service Section.')
# Image is for logo of the website.
col2.image('images\logo.png', use_column_width=True) 

# First container with 2 columns
st.subheader("The Services Provided by Textin are :") 
st.write("---") 
st.write("- THE WEBSITE IS USED TO CONVERT AUDIO AND VIDEO FILES TO TEXT.")  
col1, col2 = st.columns(2)
col1.image("images\music.png", width=80)   # audio image
col2.image("images\player.png", width=80)  # video image       
st.write("---") 


# Second container with 5 columns
st.write("- IT SUPPORTS FIVE LANGUAGES: ENGLISH, HINDI, SPANISH, FRENCH AND GERMAN.")
col1, col2, col3, col4, col5 = st.columns(5)
col1.image("images\eng.png", width=70)         # english language image
col2.image("images\hindi.png", width=70)       # hindi language image
col3.image("images\spanish.png", width=70)     # spanish language image
col4.image("images\ex.png", width=70)          # french language image
col5.image("images\german.png", width=70)      # german language image
st.write("---")



# Third container with 2 columns, each with sub-columns
st.write("- IT SUPPORTS DIFFERENT FILE FORMATS FOR AUDIO/VIDEO TO TEXT TRANSCRIPTION.")
col1, col2 = st.columns(2)
col1.write("- MP3, WAV, AND M4A FILES ARE SUPPORTED FOR AUDIO.")
col1_sub1, col1_sub2, col1_sub3 = col1.columns(3)
col1_sub1.image("images\mp3.png", width=60)     # mp3 image
col1_sub2.image("images\wav.png", width=60)     # wav image
col1_sub3.image("images\m4a.png", width=60)     # m4a image



col2.write("- MP4 AND MOV FILES ARE SUPPORTED FOR VIDEO.")
col2_sub1, col2_sub2 = col2.columns(2)
col2_sub1.image("images\mp4.png", width=60)         # mp4 image
col2_sub2.image("images\mov-file.png", width=60)    # mov image
st.write("---")

# Fourth container with 2 columns
st.write("- THE TRANSCRIPTED TEXT CAN BE DOWNLOADED IN TWO FILE FORMATS: TXT AND WORD.")
col1, col2 = st.columns(2)
col1.image("images\h.png", width=70)        # txt  image 
col2.image("images\word.png", width=70)     # word image
st.write("---")

# Fifth container with 3 columns
col1, col2 = st.columns(2)
col1.write("- THE TRANSCRIPTED TEXT IS SAVED TO THE DATABASE AUTOMATICALLY, AND THE USER CAN ALSO EDIT, UPDATE, AND DELETE IT.")
# database image
col2.image("images\database.png", width=80)     
st.write("---")





