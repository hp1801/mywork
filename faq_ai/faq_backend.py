from flask import Flask, request, jsonify
import json
from sentence_transformers import SentenceTransformer, util
import numpy as np

app = Flask(__name__)

# Load FAQ data from JSON file
with open('faq.json', 'r') as file:
    faq_data = json.load(file)['faqs']

# Load a pre-trained sentence transformer model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Precompute embeddings for all FAQ questions
faq_questions = [item['question'] for item in faq_data]
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

@app.route('/search', methods=['GET'])
def search():
    # Get the search query from the request
    query = request.args.get('query', '').lower()

    if not query:
        return jsonify({"error": "Query is empty"}), 400

    # Encode the query into an embedding
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Compute cosine similarity between the query and FAQ questions
    similarities = util.cos_sim(query_embedding, faq_embeddings)[0]
    
    # Set a similarity threshold (you can adjust this value)
    similarity_threshold = 0.5  # Example threshold

    # Get the index of the highest similarity score
    top_index = np.argmax(similarities).item()
    top_similarity = similarities[top_index].item()

    # Check if the highest similarity score meets the threshold
    if top_similarity < similarity_threshold:
        return jsonify({"message": "Can't show an answer for your query."}), 404

    # Retrieve the most relevant FAQ item
    results = [faq_data[top_index]]

    # Return the results as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app