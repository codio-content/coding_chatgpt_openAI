import os
import openai
import secret
openai.api_key=secret.api_key
### CODIO SOLUTION BEGIN
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a coding assistant with expertise in Python."},
        {"role": "user", "content": "Write a Python function to find the factorial of a given number using recursion."}
    ]
)

print(response['choices'][0]['message']['content'].strip())
### CODIO SOLUTION END