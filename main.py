import subprocess
from services.open_ai_service import improve_grammar
import os
from dotenv import load_dotenv

import logfire

load_dotenv()

logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))


# Use absolute paths
PBPASTE = "/usr/bin/pbpaste"
PBCOPY = "/usr/bin/pbcopy"

try:
    # Get the current clipboard content
    clipboard_process = subprocess.run(PBPASTE, text=True, capture_output=True)
    clipboard_content = clipboard_process.stdout.strip()

    # Process the content
    processed_content = improve_grammar(clipboard_content)
    processed_content = processed_content.improved_text

    # Copy the result back to clipboard
    copy_process = subprocess.run(PBCOPY, text=True, input=processed_content)
    logfire.info("Copied content to clipboard")

except Exception as e:
    logfire.error("Error in script: {error}", error=e)

# print(f"{processed_content}")  # Optional: Show output in terminal
# HOla Jose, espero qeu estes bien. Te quqeira preguntar de el projexto de la empresa.
