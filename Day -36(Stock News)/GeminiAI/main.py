import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY="AIzaSyDO9LUiGTWHrVfI_7XGQ1GVg9QfnHK_PQk"

# Configure Gemini AI with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Select the model (e.g., 'gemini-pro')
selected_model_name = 'gemini-pro'
model = genai.GenerativeModel(selected_model_name)

# Generate text from user input
user_input = input("Ask anything: ")

# Generate content using the model
response = model.generate_content(user_input)

# Display the response in Markdown format
print(to_markdown(response.text))


