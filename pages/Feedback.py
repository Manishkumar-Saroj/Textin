import streamlit as st  


#--------------------------------SET PAGE CONFIGRATION---------------------------- 
st.set_page_config(
    page_title="Textin",
    layout="wide",    
    initial_sidebar_state="auto"
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

#-------------------------------------MAIL FORM-----------------------------------------------------
# Load an image from a file 
image = open("images\marketing.png", "rb").read()

# Create a two-column layout with the image on the right
col1, col2 = st.columns([4,2])

# Display the image on the right side with a width of 300 pixels
with col2:
    st.image(image, width=250)


with col1:
    st.header("📬 Get In Touch With Me!")


    Feedback = """
    <form action="https://formsubmit.co/manishsaroj0907@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(Feedback, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("feedback.css")
