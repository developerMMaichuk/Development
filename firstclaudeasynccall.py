import asyncio
import anthropic

async def main():
    client = anthropic.AsyncAnthropic()

    message = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Explain NIST SP 800-207 briefly."}
        ],
    )
    print(message.content[0].text)

asyncio.run(main())
