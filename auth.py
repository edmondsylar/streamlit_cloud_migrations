import streamlit as st
import streamlit_authenticator as st_auth
from controllers.database import Database

def authenticated(func):
    """Decorator function to check if the user is authenticated."""
    def wrapper(*args, **kwargs):
        if auth.authenticate():
            return func(*args, **kwargs)
    return wrapper

@authenticated
def my_protected_function():
    """Function that can only be accessed by authenticated users."""
    st.write("Hello, authenticated user!")

# initiate database connection.
db = Database("auth_db.db")
