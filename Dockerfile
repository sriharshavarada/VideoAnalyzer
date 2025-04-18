FROM n8nio/n8n

USER root
RUN apk add --no-cache python3 py3-pip

RUN pip3 install youtube-transcript-api

COPY get_YouTubeTranscript.py /scripts/get_transcript.py

USER node
