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
        "images": ["agro.jpeg"],  # Add paths to your images
        "motivation": "Overall, literature is almost silent on how climate change affects soil temperature and its significant affect towards plant growth. ",
        "link": "manuscript under review",
    },
    {
        "name": "Occlusion-Aware Face Recognition",
        "subtitle": "Enhancing face recognition algorithms to accurately identify faces even under partial obstructions",
        "description": "A dataset comprising images of occluded faces, encompassing various types and degrees of occlusion is curated. Through extensive experimentation and evaluation on benchmark datasets,the effectiveness of our proposed method in improving recognition accuracy and robustness to occlusion is demonstrated. ",
        "images": ["dnn.jpeg"],  # Add paths to your images
        "motivation": "Bringing reliably identify individuals, even in scenarios with obstructed facial features, benefitting security and accessibility.",
        "link": "manuscript under preparation",
    },
    {
        "name": "Financial Distress Prediction",
        "subtitle": "Utilizing machine learning to forecast potential financial instability in banks.",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "images": ["agro.jpeg"],  # Add paths to your images
        "motivation": "Overall, literature is almost silent on how climate change affects soil temperature and its significant affect towards plant growth.",
        "link": "internship project",
    },
    {
        "name": "MCQ generator",
        "subtitle": "A system that automatically generates Multiple-Choice Questions using Whisper API",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "images": ["agro.jpeg"],  # Add paths to your images
        "motivation": "Provide students with opportunities for active learning and assessment during the lecture and improve online education by enhancing video lectures",
        "link": "under publication",
    },
     {
        "name": "CricBot",
        "subtitle": "A discord bot that gives the cricket score for matches of India around the world.",
        "description": "!recent command gives updates on the scores of the recent cricket match, !live command gives the live score. Data has been scraped from www.cricbuzz.com using BeautifulSoup, a Python module for extracting data from HTML and XML files.",
        "images": ["agro.jpeg"],  # Add paths to your images
        "motivation": "Provide cricket enthusiasts with instant score updates and insightful match analysis and bridging the gap between fans and the game.",
        "link": "under publication",
    },
     {
        "name": "Jake Bot",
        "subtitle": "Bringing the comedic genius of Jake Peralta from Brooklyn 99 to life through a fun and interactive chatbot experience.",
        "description": "A Python-coded Discord bot that chats like Jake Peralta from the comedy television series Brooklyn 99. Jake's dialogues were used from Brooklyn 99(Season1-4) script. The chatbot interacted with individuals who shared the same attitude and behaviour using the Microsoft DialoGPT small model.",
        "images": ["agro.jpeg"],  # Add paths to your images
        "motivation": "Designed to easy digital interactions on Discord, offering users an engaging and entertaining conversational experience with wit and humour",
        "link": "under publication",
    },
    {
        "name": "EcoBot",
        "subtitle": "Delivering environmental news from Reddit to raise awareness and promote sustainable practices.",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "images": ["agro.jpeg"],  # Add paths to your images
        "motivation": "Overall, literature is almost silent on how climate change affects soil temperature and its significant affect towards plant growth.",
        "link": "under publication",
    },

    # Add details for other projects here...
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
            for img_path in project["images"]:
                st.image(img_path, caption="", use_column_width=True)
            st.write(f"{project['description']}")

        st.write(f"**Motivation:** {project['motivation']}")
        st.write(f"**Link:** {project['link']}")

        st.write("---")  # Add a separator between projects

footer = """
    <div style="background-color: #8C95E6; color: white; text-align: center; padding: 10px;">
        <h4>Contact Details</h4>
    </div>
"""

st.markdown(footer, unsafe_allow_html=True)

