import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))
MODEL = os.getenv("LLM_MODEL")


def ask_llm(message):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content


def main():
    question = input("You: ")
    answer = ask_llm(question)
    print("Finly:", answer)


if __name__ == "__main__":
    main()