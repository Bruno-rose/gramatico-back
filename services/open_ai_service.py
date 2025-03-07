import openai
import os

from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Configure OpenAI API
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class GrammarResponse(BaseModel):
    original_text: str
    improved_text: str
    success: bool
    error_message: Optional[str] = None


def improve_grammar(text: str) -> GrammarResponse:
    """
    Improve the grammar of the provided text using OpenAI API

    Args:
        text (str): The text to improve

    Returns:
        GrammarResponse: Original and improved text with status information
    """
    # Verify API key is set
    if not os.getenv("OPENAI_API_KEY"):
        return GrammarResponse(
            original_text=text,
            improved_text=text,
            success=False,
            error_message="OpenAI API key not configured",
        )

    try:
        prompt = f"""
        Please improve the grammar and clarity of the following text while maintaining its original meaning and language.
        Only return the improved text without any explanations or additional comments.

        Text to improve:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful multilingual assistant that improves grammar and clarity of text.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,  # Lower temperature for more consistent grammar improvements
        )

        improved_text = response.choices[0].message.content.strip()

        return GrammarResponse(
            original_text=text, improved_text=improved_text, success=True
        )

    except openai.RateLimitError:
        return GrammarResponse(
            original_text=text,
            improved_text=text,
            success=False,
            error_message="OpenAI API rate limit exceeded",
        )
    except Exception as e:
        return GrammarResponse(
            original_text=text,
            improved_text=text,
            success=False,
            error_message=f"Error improving grammar: {str(e)}",
        )


if __name__ == "__main__":
    print(improve_grammar("Helo, orld!"))
