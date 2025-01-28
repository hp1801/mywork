# FAQ Assistant

The **FAQ Assistant** is a web application designed to help users find answers to common questions about a product or service. By leveraging natural language processing (NLP) techniques, this application allows users to input their queries and receive relevant answers from a predefined FAQ dataset.

## Features

- **User-Friendly Interface**: Built using Streamlit for an interactive experience.
- **Search Functionality**: Users can enter questions and receive answers based on semantic similarity.
- **Responsive Design**: The application adapts to various screen sizes for optimal viewing.
- **Loading States**: Visual feedback is provided while searching for answers.
- **Error Handling**: Basic error handling for empty queries and no results found.

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Flask
- **Natural Language Processing**: Sentence Transformers for semantic search
- **Data Storage**: JSON file for FAQs

## Installation

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine.

### Clone the Repository

git clone https://github.com/hp1801/mywork/faq1.git
cd faq-assistant


### Create a Virtual Environment

1. python -m venv venv
2. source venv/bin/activate OR Windows use: venv\Scripts\activate


### Install Dependencies

pip install -r requirements.txt
### Running the Flask Backend

python faq_backend.py

### Run the Streamlit application in another terminal:
streamlit run faq_frontend.py

### Searching for FAQs

1. Enter your question in the input field.
2. Click the "Search" button to retrieve relevant FAQs.
3. If no relevant answer is found, a message will indicate that no answer could be provided.


### EXAMPLE:
 1. In search type return policy
 2. After clicking search this is the result :
    Search Results:
    Q: What is your return policy?
    A: We offer a 30-day return policy for all products in original condition. Returns are free for defective items.
