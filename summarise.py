import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read().strip()

API_KEY = open_file('C:/Users/asus/Documents/keys/openAiApiKey.txt')
openai.api_key = API_KEY

def summarize_file(filepath):
    with open(filepath, 'r') as infile:
        text = infile.read()

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=400,
        n = 1,
        temperature=0.5,
    )

    summary = response["choices"][0]["text"]

    return summary
    
filepath = "C:/PythonProjects/summarisingTextGpt3/story.txt"
summary = summarize_file(filepath)
print(summary)