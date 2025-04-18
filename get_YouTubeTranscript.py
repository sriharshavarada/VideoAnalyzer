from youtube_transcript_api import YouTubeTranscriptApi
import sys
import json

video_id = sys.argv[1]

# Prioritize English, then Telugu, Hindi, Kannada, Tamil, etc.
preferred_languages = ['en', 'te', 'hi', 'kn', 'ta']

# ✅ Add a working proxy (can rotate/test others later)
proxies = {
    'http': 'http://103.179.109.62:8080',
    'https': 'http://103.179.109.62:8080'
}

try:
    transcript = YouTubeTranscriptApi.get_transcript(
        video_id,
        languages=preferred_languages,
        proxies=proxies  # 🆕 Add this line
    )
    text = ' '.join([entry['text'] for entry in transcript])
    print(json.dumps({ "transcript": text }))
except Exception as e:
    print(json.dumps({ "error": str(e) }))
