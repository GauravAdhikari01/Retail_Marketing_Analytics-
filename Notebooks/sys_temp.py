import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api_error_use_new_api")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-20b"
role="user"
prompt="Suggest a name for food company"

message_system={
    "role":"system",
    "content":"You are brand manager who suggest name for my food compant , name should be one word, and suggest one name only"
}

#message mai role aur content
message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]
## Temperature by default is 0 meaning safe mostly range (0,2)
response=client.chat.completions.create(model=model,messages=messages,temperature=2)

##print(response)

print("####################################")

answer=response.choices[0].message.content
print(answer)