from youtube_transcript_api import YouTubeTranscriptApi
from google import genai


#client= genai.Client(api_key="AQ.Ab8RN6LdSk-LVYWITFGk8KwWexoqJaydolrzZkYK-8qn7W_1Ug")
genai.api_key = 'Your APi key'

url = 'https://www.youtube.com/watch?v=UCGaKvZpJYc'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])


output=" "

for x in transcript:
    sentence = x.text
    output += f' {sentence}\n'

response = genai.ChatCompletion.create(
   model="gemini-2.0-flash",
   contents =[
    {"role": "system", "content": "You are a journalist."},
    {"role": "assistant", "content": "write a 100 word summary of this video"},
    {"role": "user", "content": output}
   ]
)

summary = response["choices"][0]["message"]["content"]
summary = response.text

response = genai.ChatCompletion.create(
  model="gemini-2.0-flash",
  contents =[
   {"role": "system", "content": "You are a journalist."},
   {"role": "assistant", "content": "write a 100 word summary of this video"},
   {"role": "user", "content": output}
 ]
)
tag = response["choices"][0]["message"]["content"]

print('>>>SUMMARY:')
print(summary)
print('>>>TAGS:')
print(tag)
print('>>>OUTPUT:')
