import streamlit as st
st.title(" hansika")
st.header("btech") 
st.subheader("cse(aiml)")
st.text("she is studying rcet kanyakumari")
st.markdown("##### this is her strength")
st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
st.write("Text with write")



# Writing python inbuilt function range()
st.write(range(10))
from PIL import Image  # Import Image from Pillow
img = Image.open("streamlit.jpeg") # Open the image file
st.image(img, width=500) # Display the image with a specified width





# Display a checkbox with the label 'Show/Hide'
if st.checkbox("click to 👁️ her contact "):



    # Show this text only when the checkbox is checked
    st.text("📞8217781577")


# Create a radio button to select gender
status = st.radio("Select Gender:", ['Beautiful', 'Boring'])



# Display the selected option using success message
if status == 'Beautiful':
    st.success("❤️")
else:
    st.error("😔")




# Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Her HOBBIES:", ['💃', '📚', '🎾'])


# Display the selected hobby
st.write("Her hobby:", hobby)



# Create a multiselect box for choosing hobbies
hobbies = st.multiselect("Her skills:", ['python', 'crafts', 'cooking','Makeup artist'])


# Display the number of selected hobbies
st.write("you clicked", len(hobbies), "skills")




# A simple button that does nothing
st.button("Click down")



# A button that displays text when clicked
if st.button("""Hi, I’m Hansika. I’m an AIML student who is interested in technology, especially Artificial Intelligence, Machine Learning, and Python.

I’m currently improving my programming skills by learning DSA, Python, and Machine Learning. I enjoy building practical projects and exploring new ideas, especially AI-based projects. I’m also interested in participating in hackathons because I like solving real-world problems and turning ideas into working prototypes.

Apart from academics, I’m also interested in creative things like content creation and exploring new ideas. I’m someone who likes to learn by doing rather than just studying theory. When I face a problem or make a mistake, I try to understand what went wrong and learn from it.

My goal is to become a skilled AI/ML professional and build useful technology that can solve real-world problems.
"""):
    st.text("About me ☻!")




# Create a text input box with a default placeholder
name = st.text_input("Enter her name", "Type here...")



# Display the name after clicking the Submit button
if st.button("Submit"):
    result = name.title()  # Capitalize the first letter of each word
    st.success(result)





# Create a slider to select a level between 1 and 5
level = st.slider("Choose her confidence level", min_value=1, max_value=10)


# Display the selected level
st.write(f"Selected confidence level: {level}")