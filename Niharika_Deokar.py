import streamlit as st

import streamlit as st

st. set_page_config(layout="wide")
# Define the header content
header = """
    <div style="background-color: #8C95E6; color: white; padding: 20px;">
        <h1>Niharika Deokar</h1>
        <p><b>Passionate about leveraging technology for positive change, I thrive in the intersection of data science, sustainability, and innovation. With a background in Computer Science and a deep-seated commitment to environmentalism, I'm driven to find data-driven solutions and bring innovative ssolutions to pressing climate challenges. I'm poised to make meaningful contributions to a greener, more connected world.</b></p>
    </div>
"""
st.markdown(header, unsafe_allow_html=True)

custom_css = """
    <style>
        .centered-text {
            text-align: center;
            color: #333333; /* Dark gray color */
        }
    </style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown("<h3 style='color: grey;'>Data Science Projects</h3>", unsafe_allow_html=True)


# Define project details
projects = [
    {
        "name": "AgrowMore",
        "subtitle": "Mitigating Climate Chaneg Impact Through Smart Agriculture: Soil Temperature Prediction and Analysis",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "image": "data/agro.jpeg",  # Add paths to your images
        "motivation": "Overall, literature is almost silent on how climate change affects soil temperature and its significant affect towards plant growth. ",
        "link": "manuscript under review",
        "address":"",
    },
    {
        "name": "Occlusion-Aware Face Recognition",
        "subtitle": "Enhancing face recognition algorithms to accurately identify faces even under partial obstructions",
        "description": "A dataset comprising images of occluded faces with various types and degrees of occlusion is curated. Through extensive experimentation and evaluation on benchmark datasets,the effectiveness of our proposed method is improving its recognition accuracy. ",
        "image": "data/dnn.jpeg",  # Add paths to your images
        "motivation": "Bringing reliably identify individuals, even in scenarios with obstructed facial features, benefitting security and accessibility.",
        "link": "manuscript under preparation",
         "address":"",
    },
    {
        "name": "Financial Distress Prediction",
        "subtitle": "Utilizing machine learning to forecast potential financial instability in banks.",
        "description": "This project endeavors to empower businesses with predictive analytics, enabling them to anticipate and navigate potential financial challenges, thereby fostering resilience and informed decision-making.",
        "image": "data/fin.jpeg",  # Add paths to your images
        "motivation": "In an ever-changing economy, having the foresight to address financial distress is crucial for business resilience and longevity.",
        "link": "internship project",
         "address":"",
    },
    {
        "name": "MCQ generator",
        "subtitle": "A system that automatically generates Multiple-Choice Questions using Whisper API",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "image": "data/mcq.jpeg",  # Add paths to your images
        "motivation": "Provide students with opportunities for active learning and assessment during the lecture and improve online education by enhancing video lectures",
        "link": "GitHub",
         "address":"https://github.com/deokarniharika/MCQ-generator",
    },
     {
        "name": "CricBot",
        "subtitle": "A discord bot that gives the cricket score for matches of India around the world.",
        "description": "!recent command gives updates on the scores of the recent cricket match, !live command gives the live score. Data has been scraped from www.cricbuzz.com using BeautifulSoup, a Python module for extracting data from HTML and XML files.",
        "image": "data/cric.jpeg", 
        "motivation": "Provide cricket enthusiasts with instant score updates and insightful match analysis and bridging the gap between fans and the game.",
        "link": "GitHub",
         "address":"https://github.com/deokarniharika/CricBot",
    },
     {
        "name": "Jake Bot",
        "subtitle": "Bringing the comedic genius of Jake Peralta from Brooklyn 99 to life through a fun and interactive chatbot experience.",
        "description": "A Python-coded Discord bot that chats like Jake Peralta from the comedy television series Brooklyn 99. The dataset comprises of various characters dialogues in Season1-4 script. It interacts with individuals using the Microsoft DialoGPT small model.",
        "image": "data/jake.jpeg",  
        "motivation": "Designed to ease digital interactions on Discord, offering users an engaging, witty and entertaining conversational experience.",
        "link": "GitHub",
         "address":"https://github.com/deokarniharika/Chat-Bot",
    },
    {
        "name": "InTheEco Bot",
        "subtitle": "Delivering environmental news from Reddit to raise awareness and promote sustainable practices.",
        "description": "InTheEco serves as a bridge to Reddit's environmental community. It curates and shares the latest posts related to the environment, ensuring that users remain informed and engaged with the pressing ecological issues of our time.",
        "image": "data/eco.jpeg",  
        "motivation": "Understanding the growing interest in environmental matters, this bot has been coded to make environmental news available in servers.",
        "link": "GitHub",
         "address":"https://github.com/deokarniharika/InTheEco",
    },
    {
        "name": "Digit Recognition",
        "subtitle": "Precise identification of handwritten digits by advanced ML models, enabling automation in various domains.",
        "description": "TensoFlow, NumPy, Matplotlib and Keras are the libraries used here. A convolutional neural network implements the digit recognition and the accuracy of the model increases if the number of training examples are increased.",
        "image": "data/digit.jpeg", 
        "motivation": "Enhancing efficiency and accuracy in tasks involving handwritten numerical data, from document processing to data entry.",
        "link": "GitHub",
         "address":"https://github.com/deokarniharika/digit-recognition",
    },
     {
        "name": "Sentiment Analysis",
        "subtitle": "Extracting Customer Sentiment Insights with TextBlob, a python library that preprocesses textual data.",
        "description": "Employing TextBlob, a Python library, this project analyzes customer feedback data to extract sentiments. By categorizing sentiments as positive, negative, or neutral, businesses gain actionable insights for refining products and services",
        "image": "data/sentiment.jpeg", 
        "motivation": "Performing sentiment analysis to extract valuable insights from customer feedback, enabling data-driven decisions for businesses.",
        "link": "Kaggle",
         "address":"https://www.kaggle.com/code/niharikadeokar/sentiment-analysis-using-textblob",
    }
    #added details to all projects
]

# Define layout
col1, col2, col3 = st.columns(3)

for i, project in enumerate(projects):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:

        st.write(f"##### {project['name']}")
        st.markdown(f"""
            <div style="background-color: #ccddff; padding: 10px; border-radius: 10px;">
                <p>{project['subtitle']}</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("Description"):
            # Add the image inside the expander
            st.image(project['image'], caption="", use_column_width=True)
            st.write(f"{project['description']}")

        st.write(f"**Motivation:** {project['motivation']}")
        if 'address' in project and project['address']:
            st.write(f"**Link:** [{project['link']}]({project['address']})")
        else:
            st.write(f"**Link:** {project['link']}")
        st.write("---")  # Add a separator between projects

footer = """
<div style="background-color: #B0E0E6; padding: 10px; text-align: center; max-width: 100%; position: fixed; bottom: 0; left: 0; right: 0;">
    <a href="https://www.linkedin.com/in/deokarniharika/" style="color: #000080; text-decoration: none; margin-right: 20px;">LinkedIn</a>
    <a href="https://github.com/deokarniharika" style="color: #000080; text-decoration: none; margin-right: 20px;">GitHub</a>
    <a href="https://www.kaggle.com/niharikadeokar" style="color: #000080; text-decoration: none;">Kaggle</a>
</div>
"""

# Display the footer
st.markdown(footer, unsafe_allow_html=True)
