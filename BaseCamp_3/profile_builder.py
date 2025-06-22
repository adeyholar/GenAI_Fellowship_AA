import streamlit as st

# Set page configuration for a polished look
st.set_page_config(page_title="Profile Builder", page_icon=":bust_in_silhouette:", layout="centered")

# Title and description
st.title("Profile Builder")
st.write("Create your developer profile with this interactive form!")

# Form for user input
with st.form(key="profile_form"):
    st.subheader("Your Details")
    name = st.text_input("Name", placeholder="Enter your full name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1, value=25)
    language = st.selectbox("Favorite Programming Language", ["Python", "JavaScript", "Java", "C++", "Other"])
    experience = st.radio("Experience Level", ["Beginner", "Intermediate", "Advanced"], horizontal=True)
    bio = st.text_area("Bio", placeholder="Tell us about yourself (e.g., your coding journey)")
    submit_button = st.form_submit_button("Submit Profile")

# Display results
if submit_button and name and bio:
    st.success("Profile submitted successfully!")
    st.write("### Your Developer Profile")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150", caption="Profile Picture Placeholder")
    with col2:
        st.markdown(f"**Name**: {name}")
        st.markdown(f"**Age**: {age}")
        st.markdown(f"**Favorite Language**: {language}")
        st.markdown(f"**Experience**: {experience}")
        st.markdown(f"**Bio**: {bio}")

# Sidebar for additional settings
st.sidebar.header("App Settings")
theme = st.sidebar.radio("Theme Preference", ["Light", "Dark"])
st.sidebar.write(f"Selected theme: {theme}")