import os

from groq import Groq

client = Groq(api_key="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")


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell a joke",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)