import subprocess

# Get the current clipboard content
clipboard_content = subprocess.run(
    "pbpaste", text=True, capture_output=True
).stdout.strip()

# Process the content (modify this as needed)
processed_content = clipboard_content.upper()  # Example: Convert to uppercase

# Copy the result back to clipboard
subprocess.run("pbcopy", text=True, input=processed_content)

print(f"Processed: {processed_content}")  # Optional: Show output in terminal
