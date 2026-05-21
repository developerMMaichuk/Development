import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a FICAM overview."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

print()  # newline after stream ends
