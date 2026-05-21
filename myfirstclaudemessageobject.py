# message is an anthropic.types.Message object
print(message.id)           # unique message ID: msg_...
print(message.model)        # model used: claude-sonnet-4-20250514
print(message.role)         # always 'assistant'
print(message.stop_reason)  # 'end_turn', 'max_tokens', 'stop_sequence', 'tool_use'

# content is a list of content blocks
for block in message.content:
    if block.type == "text":
        print(block.text)
    elif block.type == "tool_use":
        print(block.name, block.input)

# Token usage
print(message.usage.input_tokens)
print(message.usage.output_tokens)
