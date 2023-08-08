### FREEZE CODE BEGIN
import openai
import os

openai.api_key = os.getenv('OPENAI_KEY')
### FREEZE CODE END
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": ""},# make sure to replace empty string
        {"role": "user", "content":"" }# make sure to replace empty string
    ]
)


