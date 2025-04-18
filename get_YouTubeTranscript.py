import sys
import json
import requests
import re
import html

video_id = sys.argv[1]
SCRAPER_API_KEY = 'e5905ff90d556f0a7784b0f40eb5978e'

preferred_languages = ['en', 'te', 'hi', 'kn', 'ta']

video_url = f"https://www.youtube.com/watch?v={video_id}"
proxy_url = f"https://api.scraperapi.com?api_key={SCRAPER_API_KEY}&url={video_url}"

try:
    # Step 1: Fetch video page
    response = requests.get(proxy_url)
    if response.status_code != 200:
        raise Exception(f"ScraperAPI Error: {response.status_code}")
    html_content = response.text

    # Step 2: Extract captions JSON
    match = re.search(r'"captions":({.*?}),"videoDetails"', html_content)
    if not match:
        raise Exception("Captions not found (video may not have subtitles)")

    captions_json = json.loads(match.group(1))
    tracks = (
        captions_json.get('playerCaptionsTracklistRenderer', {})
        .get('captionTracks', [])
    )

    if not tracks:
        raise Exception("No caption tracks found")

    # Step 3: Pick first matching language
    selected_track = None
    for lang in preferred_languages:
        for track in tracks:
            if track.get('languageCode') == lang:
                selected_track = track
                break
        if selected_track:
            break

    # Step 4: Fallback to first available if no match
    if not selected_track:
        selected_track = tracks[0]

    base_url = selected_track.get('baseUrl')
    if not base_url:
        raise Exception("No baseUrl in selected track")

    # Step 5: Fetch transcript
    transcript_response = requests.get(f"https://api.scraperapi.com?api_key={SCRAPER_API_KEY}&url={base_url}")
    transcript_data = transcript_response.json()

    # Step 6: Extract text
    lines = [
        html.unescape(seg.get("utf8", ""))
        for item in transcript_data.get("events", [])
        if "segs" in item
        for seg in item["segs"]
    ]

    final_text = " ".join(lines)
    print(json.dumps({ "transcript": final_text }))

except Exception as e:
    print(json.dumps({ "error": str(e) }))

