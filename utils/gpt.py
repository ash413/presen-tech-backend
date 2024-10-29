from openai import OpenAI
from dotenv import load_dotenv

import os
import typing

load_dotenv()  # Load .env file
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def gpt_divide(text):
    prompt_templates = {
        "research_paper": "Divide this text into 6 topics: Introduction, Literature Review, Methodology, Results, Discussion, Conclusion. Each topic should have 4 points. The points should be concise and presentation-friendly.",
        "textbook": "Divide this text into chapters or sections as seen in textbooks. Each section should have concise points that are presentation-friendly.",
        "general": "Divide the text into key topics and points that are concise and suitable for a presentation format. Avoid using overly formal headings unless it's a research paper."
    }

    prompt = prompt_templates.get(doc_type, prompt_templates["general"])

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content" : prompt},
            {"role": "user", "content" : text}
    ])
    return completion.choices[0].message.content