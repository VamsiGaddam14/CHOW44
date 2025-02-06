import os
import google.generativeai as generativeai

# Configure API key
generativeai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model with settings
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = generativeai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)

# Function to generate text
def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    prompt = "Once upon a time"
    generated_text = generate_text(prompt)
    print(f"Generated Text: {generated_text}")

    # Chat session example
    chat_session = model.start_chat(history=[])
    user_input = "Tell me a short story about AI."
    response = chat_session.send_message(user_input)
    print(f"Chat Response: {response.text}")
