import streamlit as st 
from PIL import Image
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64



PAGE_TITLE = "Shahleza\'s Portfolio"

st.set_page_config(page_title=PAGE_TITLE, page_icon='👨‍🔬',layout="wide")
hide_st_style = """ <style>  #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} </style> """
st.markdown(hide_st_style, unsafe_allow_html=True)
Warning = False   

pdfFileObj = open('pdfs/Monnoo.pdf', 'rb')
profile_pic = "images/ProfilePic.png"


# --- GENERAL SETTINGS ---

NAME = "Shahleza Monnoo"
DESCRIPTION = """
Welcome to my site! \n
Let me walk you through my Projects and Skills.\n 
Adept at collaborating and leading others towards common goals, while demonstrating a high level of integrity.\n
Expertise in corporate compliance and management with proven success in the Leadership industry.\n

"""
EMAIL = "shahlezamonnoo@yahoo.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/sheharyarmonnoo/",
    "GitHub": "https://github.com/sheharyarmonnoo",
    "Twitter": "https://twitter.com",
}

sidebar_collapse = '''
 <style>


.navbar {
    position: fixed;


    flex-wrap: wrap;

    align-items: stretch;

    justify-content: space-between;
    padding: 1rem 3rem;
    background-color: #323130;
}

.navbar-brand {
    display: block;
    padding-top: .35rem;
    padding-bottom: .5rem;
    margin-right: 0rem;
    margin-left: 2.1%;
    margin-top: .01rem;
    font-size: 1.25rem;
    line-height: inherit;
    white-space: nowrap;
}


.css-1adrfps {
    background-color: rgb(240, 242, 246);
    background-attachment: fixed;
    flex-shrink: 0;
    height: calc(100vh - 2px);
    top: 2px;
    overflow: auto;
    padding: 6rem 1rem;
    position: unset;
    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
    width: 21rem;
    z-index: 1000021;
    margin-left: 0px;
}

.navbar-dark .navbar-toggler {
    color: #323130;
    border-color: #323130;
}
.navbar-toggler-icon {
    display: none;
    width: 0em;
    height: 0em;
    margin-left: 2.1%;
    margin-top: .01rem;
    vertical-align: middle;
    content: "";
    background: no-repeat center center;
    background-size: 0;
}


.css-9s5bis {
    display: fixed;
   
    align-items: center;
  
    justify-content: center;
    font-weight: 400;
    border-radius: 0.0rem;
    margin-right: 0rem;
    margin-left: 50%;
    margin-top: .8rem;
    color: white;
    width: auto;
    user-select: none;
    background-color: transparent;
    border: none;
    padding: none;
    font-size: 14px;
    line-height: 3;
}


 </style> 
 '''


st.markdown('''<link rel="stylesheet" 
            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
            crossorigin="anonymous">''', unsafe_allow_html=True)

st.markdown(sidebar_collapse, unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark">
<a class="navbar-brand" href="" target="_blank">Shahleza Monnoo</a>
</div>
</nav>
""", unsafe_allow_html=True)

@st.cache
def third_graph():    
        col = pd.read_csv('Quant_Research_2.csv')

        labels = ["Caffeine", "Taste", "Effectiveness"]

        # Create subplots: use 'domain' type for Pie subplot
        fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
        fig.add_trace(go.Pie(labels=labels,values=col[col['Type'] == 'Light Drinkers']['Count'], title="Light Drinkers"),
                    1, 1)
        fig.add_trace(go.Pie(labels=labels,values=col[col['Type'] == 'Heavy Drinkers']['Count'], title="Heavy Drinkers"),
                    1, 2)

        # Use `hole` to create a donut-like pie chart
        fig.update_traces(hole=.4, hoverinfo="label+percent+name")

        fig.update_layout(
            title_text="",width = 1500,height = 700

            # Add annotations in the center of the donut pies.
        )
            
        return fig

@st.cache
def first_graph():    
    d = ['For Fun',"I do not drink energy drinks","Others","Social Activities","Utility (work, study, etc.)","Working out"]
    e = [10,15,3,11,30,15]
    grp = pd.DataFrame({'Type':d,'Count':e})

    fello = px.bar(
        grp.sort_values(by= 'Count'),
        x='Count',
        y='Type'       
        )

    fello.update_layout(title = "",
        template = 'simple_white', xaxis_title = '', 
        yaxis_title = '', width = 1500, height = 700
        ,yaxis = dict(tickfont = dict( size = 15  ))
        ,xaxis = dict(tickfont = dict( size = 20  )))
    
    return fello

@st.cache
def second_graph():    
    col = pd.read_csv('Quant_Research.csv')

    ggg = px.bar(
        col.sort_values(by= ['Type']),
        x='Category',
        y='Count',
        
        # color_discrete_sequence =['dark red'],
        color='Type', barmode="group"
        
        # color_discrete_sequence =['dark red'],
        
        )

    ggg.update_layout(title = "",
        template = 'simple_white', xaxis_title = '', 
        yaxis_title = '', width = 1500, height = 700
        ,yaxis = dict(tickfont = dict( size = 15  ))
        ,xaxis = dict(tickfont = dict( size = 20  )))
    
    return ggg

def pad(x):
    
    for i in range(x):
        st.markdown("\n")

profile_pic = Image.open(profile_pic)


# # --- HERO SECTION ---

with st.sidebar:
        selected_option = option_menu(
        menu_title = 'Navigation',
        menu_icon = ' ',
        # icons = ['broadcast-pin', 'unlock', 'umbrella'],
        options = ['Summary','Redbull', 'OPUS'],
        styles = {
            "container": {"padding": "5px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "#323130"}
            
            } )


        
if selected_option == "Summary":
                  


    with st.container():
        _ , col1, _, col2, _ = st.columns([.7,1,.0001,1,.4])
        with col1:
            st.image(profile_pic, width=320)
            st.markdown("")
        with col2:
            st.markdown("# Hi!\n### Welcome to my Portfolio\n ### I am excited to walk you through my work!")
            st.markdown("#### Please feel free to use the navigation on the **left** to cycle through my projects")
            

    with st.container():
        _, col1, _ = st.columns([.2,1,.2])
        with col1:
        
            
            st.markdown("---")
            pad(3)
            
            st.title("My Timeline for Projects")        
            st.markdown("##### A short timeline representing my inspiration and sequence of work")
            
            pad(5)
            with st.spinner(text="Building line"):
                
                with open('styles/timeline.json', "r") as f:
                    data = f.read()
                    timeline(data, height=700)
            
            st.markdown("---")
            

if selected_option == "Redbull":
        _, col1, _ = st.columns([.2,1,.2])
        
        with col1:
        
            
            st.title("The Red Bull Case")     
            pad(3)   

            st.markdown("""
        
        
        <h4>
            <b>1. Summary</b>
        </h4>
        <p>
            RedBull was founded in 1987 and is distributed in 171 countries. It is currently valued at <b>$17.54Bn</b>
            and had net sales of <b>$2.89Bn</b> in 2021 with over <b>75Bn</b> cans sold.<br> Main source of <b>brand awareness</b> is through <b>sponsoring events</b> including sport tournments, nightclub events and even voluteer events for special.

        </p>
        <br>
        <br>
        <h4>
            <b>2. Analysis Plan</b>

        </h4>
        <p>
            Utlizing a dataset of 30min interviews with undergrads, we take all variables from the conversativons and identify the most important features for chooses Redbull over other energy drinks.<br>
            We are also working with a dataset of online reviews from sources such as Amazon.com, Walmart.com, Instagram, Facebook and Twitter to identify a common pattern of choice between these customers.
            <br>
            <br>  
            <br>              
            Here are the steps for excecuting this plan:
        </p>


                        """,unsafe_allow_html=True)
            
            st.markdown("""
        
        
                
                <li><b>Consolidate all customer data</b> in one data model and choose important / common features </li> 
                <br>
                
                <li>Run analysis to <b>find correlation </b>between variables and eliminate un-important variables</li>
                <br>
                <li>Rank variables from most important and identify <b>customer segment</b> that responds most closely to them</li>
            
        


                        """,unsafe_allow_html=True)
            
            pad(5)
            
            st.markdown("#### **Category Breakdown**")
            
            st.plotly_chart(first_graph())
            
            
            st.markdown("""
                        
                        
                        
                                <p>
            It is clear from this chart that the <b>most common response</b> from our data falls within the <b>Utility</b> category. There might have been bias within our data since most of the demographic distribution is college students.<br>
            However, college students still remain a huge part of the energy drinks segment as almost all campuses nationwide have Redbull sponsored events held annually.
            Therefore, this information is still useful in penerating the college student market. 
            
            

        
    </p>
                        
                        """
                        
                        
                        
                       ,unsafe_allow_html=True )
            
            
            pad(5)
            st.markdown("#### **Perception Analysis**")
            st.plotly_chart(second_graph())
            pad(5)
            
            st.markdown("""
                        
                            <p>
       People who prefer Redbull generally enjoy how effective it is and also prefer the taste over other energy drinks. 
       <b>Effectiveness and Caffeine content play hand-to-hand</b> and thus the high 
       score on both for Redbull solidifies our intial findings of work/study category use.
        
                
    </p>

                        
                        """,unsafe_allow_html=True )
            
            

    
            pad(5)
            st.markdown("#### **Heavy Energy Drinkers feel neutral about the taste**")        
            st.plotly_chart(third_graph())

            st.markdown("""
                            <p>
        After narrowing down the segments within Redbull's customer demographic, we identified the heavy drinkers don't have a 
        preference to taste as compared to light drinkers.

     <br>
     <br>
     <h3>
        Conclusion and Recommendations
     </h3>
     </p>
     <br>
     
         """,unsafe_allow_html=True)
                   
     
            st.markdown("""

     <li><b></b> Red Bull is preferred due to its <b>High Effectiveness</b> and <b>Caffeine Content</b> but not its taste</li> 
     <br>
     
     <li>Mangement should <b>focus</b> on developing marketing campaigns <b>highlighting RedBull's strong effectiveness</b> and illustrate scenarios of work / study consumptions</li>
     <br>
     <li>Even though other segments aside from Utlities remains a market for RedBull, the <b>customer acquistion cost</b> for that segment is higher compared to Utility work.</li>
     <br>
     <li>Marketing should refrain showcasing social activites (nightclubs / partying) due to lower potential <b>Customer Lifetime Value<b>.</li>
     
     
     
     
 


                        
                        """,unsafe_allow_html=True)
            
                        
            with open("Brand equity presentation.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
               
            pad(5)
            st.download_button(label="Download Presentation File", 
                    data=PDFbyte,
                    file_name="RedBull_CASE.pdf",
                    mime='application/octet-stream')
            
            
            

            
            
            
            
if selected_option == "OPUS":
        _, col1, _ = st.columns([.2,1,.2])
        
        with col1:
        
            
            st.title("OPUS Coffee")     
            st.markdown("##### A local Coffee Shop in Gainesville, FL")
            pad(3)   

            st.markdown("""
        
        
        <h4>
            <b>1. Aim of Analysis</b>
        </h4>
        <p>
            OPUS is a local coffee shop in Gainesville with 9 stores in total. <br><br>We are hired by management to come up with a marketing strategy to increase revenue</b>
            and provide a general understanding of customer brand preferences for Coffee Shops.

        </p>
        <br>
        <br>
        <h4>
            <b>2. Approach</b>

        </h4>
        <p>
            <li>We aim to understand customer loyalty for Coffee shops among consumers and what features are preferred by customers<\li>  
            <br>  
            <li>We recommended new programs such as free rewards for points aimed at increasing customer Customer Life Value<\li>            
            <br>
            <li>We narrated the brand position of OPUS in its current market along with techniques to increase the customer base<\li>
            <br>              
            <br>  
            Please download our presentation below for more details:
        </p>


                        """,unsafe_allow_html=True)
            
            with open("web based marketing ppt.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
               
            

            
            st.image(
            "https://s.yimg.com/bj/4f6c/4f6c0cd0b11130577694215b860b723d.jpg",
            width=800, # Manually Adjust the width of the image as per requirement
        )
                        
            pad(3)
            st.download_button(label="Download Presentation File", 
                    data=PDFbyte,
                    file_name="OPUS_CASE.pdf",
                    mime='application/octet-stream')
            