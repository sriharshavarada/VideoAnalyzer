from youtube_transcript_api import YouTubeTranscriptApi
import sys
import json

video_id = sys.argv[1]

# Prioritize English, then Telugu, Hindi, Kannada, Tamil, etc.
preferred_languages = ['en', 'te', 'hi', 'kn', 'ta']

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=preferred_languages)
    text = ' '.join([entry['text'] for entry in transcript])
    print(json.dumps({ "transcript": text }))
except Exception as e:
    print(json.dumps({ "error": str(e) }))
