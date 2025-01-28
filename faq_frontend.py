import streamlit as st
import requests

# Title of the app
st.title("FAQ Assistant")

# Input field for the user's question
user_query = st.text_input("Ask a question:")

# Button to trigger the search
if st.button("Search"):
    if user_query:
        # Show a loading spinner while waiting for the response
        with st.spinner("Searching for answers..."):
            try:
                # Call the Flask backend API
                response = requests.get(f"http://127.0.0.1:5000/search?query={user_query}")
                
                if response.status_code == 200:
                    results = response.json()
                    if results:
                        st.write("### Search Results:")
                        for result in results:
                            st.write(f"**Q:** {result['question']}")
                            st.write(f"**A:** {result['answer']}")
                            st.write("---")
                    else:
                        st.write("No results found.")
                else:
                    st.error("Failed to fetch results from the server.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")