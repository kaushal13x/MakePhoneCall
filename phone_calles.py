import streamlit as st
from twilio.rest import Client

account_sid = 'AC9ef1c9fb4fb7446debd72046852a10ce'
auth_token = 'c3bc8d7198048a782f5c359d1cd247dd'
twilio_number = '+15109440236'

st.set_page_config(page_title="Make a Phone Call", layout="centered")

st.title("Make a Phone Call")

receiver_number = st.text_input("Enter Phone Number (with +91):", placeholder="+91XXXXXXXXXX")
voice_message = st.text_area("Enter Message to Speak on Call:", value="This is a test call from your Python app.")

if st.button("Make Call"):
    if receiver_number.startswith("+91") and len(receiver_number) == 13:
        try:
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                twiml=f'<Response><Say>{voice_message}</Say></Response>',
                from_=twilio_number,
                to=receiver_number
            )

            st.success(f"Call initiated successfully! Call SID: {call.sid}")
        except Exception as e:
            st.error(f"Failed to make the call: {e}")
    else:
        st.warning("Please enter a valid Indian number starting with +91 and 13 digits total.")
