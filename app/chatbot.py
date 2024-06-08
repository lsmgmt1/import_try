import openai

def get_bot_response(message):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    response = openai.Completion.create(
      engine="davinci",
      prompt=message,
      max_tokens=150
    )
    return response.choices[0].text.strip()
