import streamlit as st

st. set_page_config(layout="wide")

header = """
    <div style="background-color: #8C95E6; color: white; padding: 20px;">
        <h1>Niharika Deokar</h1>
        <p><b>Passionate about leveraging technology for positive change, I thrive in the intersection of data science, sustainability, and innovation. With a background in Computer Science and a deep-seated commitment to environmentalism, I'm driven to find data-driven solutions and bring innovative ssolutions to pressing climate challenges. I'm poised to make meaningful contributions to a greener, more connected world.</b></p>
    </div>
"""
st.markdown(header, unsafe_allow_html=True)

st.write("#### Data Science")

projects = [
    {
        "name": "AgrowMore",
        "subtitle": "Mitigating Climate Chaneg Impact Through Smart Agriculture: Soil Temperature Prediction and Analysis",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "images": ["agro.jpg"],  
        "motivation": "Overall, literature is almost silent on how climate change affects soil temperature and its significant affect towards plant growth. ",
        "link": "manuscript under review",
    },
    {
        "name": "Occlusion-Aware Face Recognition",
        "subtitle": "Collecting and Reconstructing occluded images for facial recognition using deep neural networks",
        "description": "A dataset comprising images of occluded faces, encompassing various types and degrees of occlusion is curated. Through extensive experimentation and evaluation on benchmark datasets,the effectiveness of our proposed method in improving recognition accuracy and robustness to occlusion is demonstarted. ",
        "images": ["agro.jpg"], 
        "motivation": "Collaborator 1",
        "link": "manuscript under preparation",
    },
    {
        "name": "Financial Distress Prediction",
        "subtitle": "Utilized different ML and statistical models to analyze the financial health of a company.",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "images": ["agro.jpg"],  
        "motivation": "Collaborator 1",
        "link": "under publication",
    },
    {
        "name": "MCQ generator",
        "subtitle": "Mitigating Climate Chaneg Impact Through Smart Agriculture: Soil Temperature Prediction and Analysis",
        "description": "The research focuses on soil temperature variationt. It demonstrates how machine learning models could assist farmers and researchers in reducing the hazards brought on by climate change and offers ideas for future research.",
        "images": ["agro.jpg"], 
        "motivation": "Collaborator 1",
        "link": "under publication",
    },

  
]

# Define layout
col1, col2, col3 = st.columns(3)

# Display projects
for i, project in enumerate(projects):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        
        st.write(f"##### {project['name']}")
        st.write(f"**-** {project['subtitle']}")

        with st.expander("Description"):
            st.write(f"{project['description']}")
        st.write(f"**Motivation:** {project['motivation']}")
        st.write(f"**Link:** {project['link']}")

    
        for img_path in project["images"]:
            st.image(img_path, caption="", use_column_width=True)

        st.write("---")  
    


footer = """
    <div style="background-color: #3F9886; color: white; text-align: center; padding: 10px;">
        <p>Contact Details</p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
