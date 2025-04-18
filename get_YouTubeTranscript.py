import sys
import json
import requests

video_id = sys.argv[1]
preferred_languages = ['en', 'te', 'hi', 'kn', 'ta']

# 🔑 Get your ScraperAPI key from https://www.scraperapi.com/dashboard
SCRAPER_API_KEY = 'e5905ff90d556f0a7784b0f40eb5978e'

# YouTube Transcript URL (used by youtube_transcript_api internally)
video_url = f"https://www.youtube.com/watch?v={video_id}"
proxy_url = f"http://api.scraperapi.com?api_key={SCRAPER_API_KEY}&url={video_url}"

try:
    # ScraperAPI will return the HTML of the YouTube page
    response = requests.get(proxy_url)
    if response.status_code != 200:
        raise Exception(f"ScraperAPI Error: {response.status_code}")

    # 👇 Pass through ScraperAPI proxy to YouTubeTranscriptApi
    from youtube_transcript_api import YouTubeTranscriptApi
    transcript = YouTubeTranscriptApi.get_transcript(
        video_id,
        languages=preferred_languages,
        proxies={
            'http': proxy_url,
            'https': proxy_url
        }
    )

    text = ' '.join([entry['text'] for entry in transcript])
    print(json.dumps({ "transcript": text }))

except Exception as e:
    print(json.dumps({ "error": str(e) }))
