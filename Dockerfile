FROM n8nio/n8n

USER root

# Install Python + dependencies
RUN apk add --no-cache \
  python3 \
  py3-pip \
  build-base \
  libffi-dev \
  openssl-dev \
  cargo \
  rust

# Install YouTube transcript API (force override system protections)
RUN python3 -m pip install --break-system-packages youtube-transcript-api

# Copy the script
COPY get_YouTubeTranscript.py /scripts/get_transcript.py

USER node
