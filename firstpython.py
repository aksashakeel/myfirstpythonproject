#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", project_icon="✨")
st.title("Growth Mindset Challange: Web App with Streamlit")

st.header("🚀 Wellcome to Your Growth Journey!")
st.write(" A simple Streamlit app that encourages users to embrace a growth mindset through interactive challenges, motivational quotes, and progress tracking! 🌟")


#qoute section
st.header("💡 Today's Growth Mindset Quote")
st.write("\"Challenges are what make life interesting; overcoming them is what makes life meaningful.\"")

st.header("What's Your Challange Today?")
User_input = st.text_input("Describe a challange you're facing:")

#condition
if User_input:
    st.success(f"💪 you are facing: {User_input}. Keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challange to get started!")    


#reflexing 
st.header("🧠 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"⭐ Great Insight! Your reflection: {reflection}")

else:
    st.info("Reflection on past experience help you grow! Share your difficulties")       


#achievements

st.header("🏆 Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")

if acheivment:
    st.success(f"🎉 Amazing You Achieved: {acheivment}")

else:
    st.info("Big or small , every acheivment counts! Share one now!🤩")

#footer
st.write("- - - ")
st.write("Keep believing in yourself.Growth is a journey,not a destination!")
st.write("©️ Created by Aqsa Shakeel")      

