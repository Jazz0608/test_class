from dotenv import load_dotenv
import os
import sys

load_dotenv()

print("Python:", sys.executable)
print("Version:", sys.version)

print("GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))
