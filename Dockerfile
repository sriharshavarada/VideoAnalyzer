FROM n8nio/n8n

USER root

# Install Python and required system dependencies
RUN apk add --no-cache \
  python3 \
  py3-pip \
  build-base \
  libffi-dev \
  openssl-dev \
  cargo \
  rust

# Install the YouTube Transcript API with override flag (PEP 668 fix)
RUN python3 -m pip install --break-system-packages youtube-transcript-api

# Copy your script to a known path
COPY get_YouTubeTranscript.py /scripts/get_transcript.py

USER node