import os
import openai
import secret
openai.api_key=secret.api_key

message=[
        {"role": "system", "content": "You are a coding assistant with expertise in JavaScript."},
        {"role": "user", "content": "I have this JavaScript code: `function add(a, b) { return a + b; }`. Can you suggest any improvements or optimizations?"}
    ]

# FREEZE CODE BEGIN
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages= message
)

print(response['choices'][0]['message']['content'].strip())

# FREEZE CODE END