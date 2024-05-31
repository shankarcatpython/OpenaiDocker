import openai
import app.config as config


def askme_questions_summarize(prompt):
 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful elucidator"},
            {"role": "user", "content": f"Summarize information about {prompt}"}
        ]
    )

    return response.choices[0].message['content']

def askme_questions_suggestion(prompt):
    response_sugg = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful counsellor"},
            {"role": "user", "content": f"Suggest about {prompt}"}
        ]
    )

    return response_sugg.choices[0].message['content']