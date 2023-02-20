from dotenv import load_dotenv, dotenv_values

# Example 1:
dotenv_values = dotenv_values()
print(dotenv_values.get("MY_VARIABLE"))

# Example 2:
load_dotenv()
import os
print(os.getenv("MY_VARIABLE"))