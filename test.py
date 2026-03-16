from google import genai

client = genai.Client(api_key="AIzaSyBbZgBWyveObmQTk_LGiBvA-DlraM3D2CI")

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Hello"
    )
    print("Success:", response.text)
except Exception as e:
    print("Error:", e)