import openai
import pyttsx3

# Set your OpenAI GPT-3 API key
openai.api_key = "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"
import time

# Set your OpenAI GPT-3 API key
# openai.api_key = 'your_api_key_here'

# Initialize text-to-speech engine
speaker = pyttsx3.init()

# Function to speak a response
def speak(text):
    speaker.say(text)
    speaker.runAndWait()

# Function to generate content using GPT-3
def generate_content(prompt):
    retries = 3  # Number of retries in case of rate limit error
    for _ in range(retries):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded. Waiting for {e.retry_after_seconds} seconds...")
            time.sleep(e.retry_after_seconds)
            continue
    raise Exception("Rate limit exceeded after retries")

# Main loop of the voice assistant
while True:
    user_input = input("Speak something: ")
    print("You said:", user_input)

    if "hello" in user_input:
        response = generate_content("Hello! How can I help you?")
        speak(response)
    elif "goodbye" in user_input:
        response = generate_content("Goodbye! Have a nice day.")
        speak(response)
        break
    elif "what is the weather today" in user_input:
        response = generate_content("I'm sorry, I can't access the internet to get the weather.")
        speak(response)
    else:
        response = generate_content("I don't understand.")
        speak(response)
