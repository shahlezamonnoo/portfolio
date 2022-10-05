import streamlit as st 
from constant import *
from PIL import Image
from streamlit_timeline import timeline



PAGE_TITLE = "Sheys\'s Portfolio"

st.set_page_config(page_title=PAGE_TITLE, page_icon='👨‍🔬',layout="wide")
hide_st_style = """ <style>  #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} </style> """
st.markdown(hide_st_style, unsafe_allow_html=True)
Warning = False   

pdfFileObj = open('pdfs/Monnoo.pdf', 'rb')
profile_pic = "images/ProfilePic.png"


# --- GENERAL SETTINGS ---

NAME = "Sheharyar Monnoo"
DESCRIPTION = """
Senior Finance Analyst, assisting enterprises by supporting data-driven decision-making.\n
Results-driven individual who is passionate about developing team and organizational culture.\n 
Adept at collaborating and leading others towards common goals, while demonstrating a high level of integrity.\n
Expertise in corporate compliance and management with proven success in the Leadership industry.\n

"""
EMAIL = "monnoo.sheharyar@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/sheharyarmonnoo/",
    "GitHub": "https://github.com/sheharyarmonnoo",
    "Twitter": "https://twitter.com",
}


def padd(x):
    
    for i in range(x):
        st.markdown("\n")

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---

with st.container():
    col , col1, _, col2 = st.columns([.8,1,.2,2])
    with col1:
        st.image(profile_pic, width=320)
        st.markdown("")

    with col2:
        st.markdown("")
        st.title(NAME)
        st.write(DESCRIPTION)   
        st.write("\n")
        # st.write("📫", EMAIL)
        st.download_button('Download Resume',pdfFileObj,file_name='Monnoo.pdf',mime='pdf')
        st.write("\n")

# --- SOCIAL LINKS ---

fixer = 10
cols = st.columns(len(SOCIAL_MEDIA)+fixer)
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[fixer-index].write(f"[{platform}]({link})")

padd(5)


with st.container():
    col , col1, _, col2 = st.columns([.8,1,.2,2])
    
    with col1:
        st.subheader('Summary')
        st.write(info['Brief'])

    with col2:
        
        
        st.subheader('Skills & Tools ⚒️')
        
        st.write(
    """
- ✔️ Advance knowledge in Python, Database and Cloud implementation
- ✔️ Intermediate understanding of statistical principles and their respective applications
- ✔️ Experience with building complex ETL pipelines, including streaming data
- ✔️ Team-player and strong sense of initiative on tasks
"""
)


padd(8)
with st.container():
    col , col1, _, col2 = st.columns([.8,1,.2,2])
    
    with col1:                  
        st.markdown('')
        st.subheader('Career Timeline')
        
with st.container():
    _ , col1, _ = st.columns([1.5,5,1])
    
    with col1:    
        with st.spinner(text="Building line"):
            with open('styles/timeline.json', "r") as f:
                data = f.read()
                timeline(data, height=700)
        st.write("\n")


padd(8)
with st.container():
    col , col1, _, col2 = st.columns([.8,1,.2,2])
    
    with col1: 
        st.subheader('Education')

padd(1)

with st.container():
    
    _ , col1, _ = st.columns([1.5,5,1])
    
    with col1:
            st.markdown("""📖 University of Oklahoma - Masters in Finance | Financial Risk Management - 2021""")
            st.markdown("""📖 University of Florida - Bachelors in Management - 2018""")
            st.write("\n")
        

padd(8)
with st.container():
    col , col1, _, col2 = st.columns([.8,1,.2,2])
    
    with col1:
        st.write("\n")
        st.subheader('Projects')

padd(3)
with st.container():
    
    _ , col1, _ = st.columns([2,5,2])
    
    with col1:

            
            with st.expander("Custom CRM System",expanded=True):
                
                st.markdown("""Built Cloud CRM platform utlizing Python's Flask as back-end, integrated with a No-SQL database, Cloud Drive Storage and Front-End in HTML/CSS.""")
                
                rca_image_gallery = './images/GraphGrid-Data-Platform-Architecture.png'
                rca_image = Image.open(rca_image_gallery)
                st.image(rca_image,width=None, use_column_width=True)
            
            padd(2)
            with st.expander("End-to-End Financial Reporting Solution",expanded=True):
                
                st.markdown("Helped Reduce Revenue Reporting Cycle from 3 weeks to 3 days. Utilized Python and SQL to create automated solution that processes raw financial data to accure revenue, expenses based on historicals and aging reports.")
                finance = './images/rpa1.PNG'
                rca_image_1 = Image.open(finance)
                st.image(rca_image_1,width=None, use_column_width=True)
        
            padd(2)
            with st.expander("Data Analyst with Python",expanded=True):
                
                st.markdown("""Rigourus test of SQL, Python Programming, Statistics, Machine Learning and a coding challenge aimed to solve real-world data problems.""")
                da = './images/DAP.png'
                rca_image = Image.open(da)
                st.image(rca_image,width=None, use_column_width=True)

padd(10)                


st.markdown('---')  
with st.container():
    _ , col1, _ = st.columns([5,2,5])
    
    with col1:                  
        st.header('Contact :mailbox:')
        
st.markdown('---')        

padd(5)
with st.container():
    _ , col1, _ = st.columns([2,5,2])
    
    with col1:    



        contact_form = """
        <form action="https://formsubmit.co/40809310289037b472a15fdf4971dbe3" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("styles/style.css")
                