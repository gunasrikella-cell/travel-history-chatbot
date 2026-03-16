from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# 🔑 Add your OpenAI API Key here (get from https://platform.openai.com/api-keys)
client = OpenAI(api_key="AIzaSyBA27AuSGp1oSAYf9uoaqx0KhDlzO7tOTo")



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    
    # Get user message
    data = request.get_json()
    user_message = data.get("message")

    # Travel chatbot prompt
    prompt = f"""
You are a travel assistant chatbot.

Answer ONLY travel related questions such as:
- tourist places
- travel guides
- hotels
- countries
- monuments
- transportation
- travel tips
- travel budget

If the question is not related to travel reply:
"I only answer travel related questions."

User question: {user_message}
"""

    try:
        # Generate response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract reply text
        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        error_str = str(e).lower()
        if "429" in error_str or "resource_exhausted" in error_str or "quota" in error_str:
            return jsonify({"reply": "You've reached the API quota limit for the free tier. Please try again later (quota resets daily) or consider upgrading to a paid plan at https://ai.google.dev/gemini-api/docs/rate-limits."})
        else:
            return jsonify({"reply": "Sorry, an error occurred: " + str(e)})

if __name__ == '__main__':
    app.run(debug=True)