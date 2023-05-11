import streamlit as st
from O365 import Account

m365_client_ID = "b00013bf-c9fe-4e0f-9d87-0ba758476640" # Application ID
m365_secrete = "979adc70-a759-4093-80d9-afc34fc907dc"


credentials = (m365_client_ID, m365_secrete)

account = Account(credentials)
# m = account.new_message()
# m.to.add('edmondmusiitwa@gmail.com')
# m.subject = 'Testing!'
# m.body = "George Best quote: I've stopped drinking, but only while I'm asleep."
# m.send()

st.write(account)