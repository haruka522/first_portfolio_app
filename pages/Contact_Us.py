import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email", placeholder="example@example.com")
    message = st.text_area("Your Message")
    message = f"Subject: Contact from {user_email}\n\n{message}"
    submit_button = st.form_submit_button("Send Message")
    if submit_button:
        send_email(message)
        st.success("Message sent successfully!")
