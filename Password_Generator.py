import streamlit as st
import re


st.set_page_config(page_title="Password Strenght Checker By Abdul Basit Khawar", page_icon="🔑",layout="centered")





st.markdown(""" 

<style>

    .main {text-align: center;}
    .stTextInput {width: 60%  !importantly; margin: auto;} 
    .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px;}               
    .stButton button:hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)


#page title and description
st.title("🔐 Password Strenght Generator")
st.write("Enter Your Password below to check its security level. 🔍")

#Function to check password strength

def check_password_strength(password):
    score = 0 
    feedback = []

    if len(password) >= 8:
        score +=1 #increase score by 1

    else:
        feedback.append("❌ Password Shuld be **at least 8 characters long**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
        score +=1

    else:
        feedback.append("❌ Password Shuld include **both upper case (A-Z) and lower case (a-z) letters**")

    if re.search(r"\d",password):
        score +=1

    else:
        feedback.append("❌ Password Shuld include **at least one digit (0-9)**")

    #special character

    if re.search(r"[!@#$%^&*]", password):
        score +=1

    else:
        feedback.append("❌ Password Shuld include **at least one special character**")

    #display password strenth result

    if score == 4:
        st.success("✅ **Strong Password** Your Password is secure.")

    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features")                                 
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strenth it.")

    #feedback

    if feedback:
        with st.expander("🔎 **Improve Your Password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔒")

#Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password fisrt!") #show warning if password emplty 


