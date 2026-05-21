import anthropic

# Instantiate the client
# ANTHROPIC_API_KEY env var is read automatically
client = anthropic.Anthropic()

# Send a message
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is Zero Trust Architecture?"}
    ],
)

# The response content is a list of content blocks
print(message.content[0].text)
