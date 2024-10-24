import requests
import androidhelper
from fuzzywuzzy import fuzz

# Initialize AndroidHelper
droid = androidhelper.Android()

# URL of Flask server
url = 'http://192.168.97.247:5000/receive_answer'

# Define the QA pairs (You can add more as needed)
qa_pairs = {
    "2 + 2": "4",
    "what is a square": "A square is a geometric shape with four equal sides",
    "what is a matrix": "A matrix is a rectangular array of numbers arranged in rows and columns.",
    "what is permutation": "Permutation is an arrangement of objects in a specific order.",
    "table of 12": "Table of 12",
    "what is factorial": "Factorial is the product of all positive integers up to a given number .",
    "what is trigonometry": "Trigonometry is the study of relationships between angles and sides of triangles.",
    "what is pythagorean theorem": "abc", 
}

def get_closest_match(user_question):
    # Use fuzzy string matching to find the closest matching question
    best_match = None
    highest_ratio = 0

    for question in qa_pairs:
        match_ratio = fuzz.ratio(user_question.lower(), question.lower())
        if match_ratio > highest_ratio:
            highest_ratio = match_ratio
            best_match = question

    # If the best match ratio is above a certain threshold (say 70), return the match
    if highest_ratio >= 70:
        return best_match
    return None

def send_answer_to_server(answer):
    # Prepare the answer data
    answer_data = {"answer": answer}

    try:
        # Send POST request to the Flask server
        response = requests.post(url, json=answer_data)

        # Handle the response status code
        if response.status_code == 204:
            print("Answer sent successfully, no content returned.")
        elif response.status_code == 400:
            print("Bad request, no answer provided.")
        else:
            print(f"Unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending the request: {e}")

def voice_to_text():
    # Use AndroidHelper to take voice input and convert it to text
    print("Please ask your question.")
    result = droid.recognizeSpeech()
    if result.result:
        return result.result
    else:
        return None

def main():
    # Get voice input from the user
    user_question = voice_to_text()

    if user_question:
        print(f"User asked: {user_question}")

        # Find the closest matching question from the predefined QA pairs
        matched_question = get_closest_match(user_question)

        if matched_question:
            # If a match is found, get the answer and send it to the server
            answer = qa_pairs[matched_question]
            print(f"Answer: {answer}")
            send_answer_to_server(answer)
        else:
            # If no match is found, send a message indicating the question is not understood
            print("Sorry, I don't understand that question.")
            send_answer_to_server("I don't understand that.")
    else:
        print("No voice input detected.")

if __name__ == "__main__":
    main()
