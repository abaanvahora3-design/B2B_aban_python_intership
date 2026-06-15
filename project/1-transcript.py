from youtube_transcript_api import YouTubeTranscriptApi

url = 'https://www.youtube.com/watch?v=NXJqHVZJ9lI'
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])

print(transcript)

output=''
for x in transcript:
  sentence = x ['text']
  output += f' {sentence}\n'

print(output)