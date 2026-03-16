from google import genai

# Add your new API key
genai.configure(api_key="AIzaSyBbZgBWyveObmQTk_LGiBvA-DlraM3D2CI")

# List all available models
models = genai.list_models()
for model in models:
    print(model.name, "->", model.supported_generation_methods)    