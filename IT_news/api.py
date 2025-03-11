# api.py

from openai import OpenAI

client = OpenAI(api_key='API_KEY')

def get_gpt_summary(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500
    )

    return completion .choices[0].message.content.strip()
