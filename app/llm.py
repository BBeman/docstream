from anthropic import AsyncAnthropic
from app.config import settings

client = AsyncAnthropic(
    api_key= settings.anthropic_api_key
)


async def summarise(text : str, max_words: int = 100) -> str:
    prompt = f"summarize {text} in a total word count of: {max_words}."
    message = await client.messages.create(
        max_tokens=1024,
        messages=[
            {
            "role" : "user",
            "content" : prompt
        }
        ],
        model= settings.model_name
    )
    return message.content[0].text