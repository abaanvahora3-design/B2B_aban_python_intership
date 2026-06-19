from youtube_transcript_api import YouTubeTranscriptApi
from google import genai

# genai.api_key = 'AQ.Ab8RN6LdSk-LVYWITFGk8KwWexoqJaydolrzZkYK-8qn7W_1Ug'

url = 'https://www.youtube.com/watch?v=UCGaKvZpJYc'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])

response = genai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {"role": "system", "content": "You are a database computer"},
    {"role": "assistant", "content": "data is stored in JSON {text:'', start:'', duration:''}"},
    {"role": "assistant", "content": str(transcript)},
    {"role": "user", "content": "what are the topics discussed in this video. Provide start time codes in seconds and also in minutes and seconds"}
  ]
)
timecode = response["choices"][0]["message"]["content"]

print(timecode)
