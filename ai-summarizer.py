from openai import OpenAI

client = OpenAI(api_key="")

print("AI Document Summarizer")
print("----------------------")

text = input("Enter a long text: ")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"Summarize this text in 2 sentences: {text}"
)

summary = response.output[0].content[0].text

print("\nAI Summary:")
print(summary)

