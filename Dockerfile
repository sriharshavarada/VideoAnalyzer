FROM n8nio/n8n

USER root

# Install Python and build tools
RUN apk add --no-cache \
  python3 \
  py3-pip \
  py3-setuptools \
  py3-wheel \
  build-base \
  gcc \
  g++ \
  libffi-dev \
  musl-dev \
  openssl-dev \
  cargo \
  rust

# Upgrade pip tools (important for some dependencies)
RUN python3 -m pip install --upgrade pip setuptools wheel

# Install the YouTube transcript library
RUN python3 -m pip install youtube-transcript-api

# Copy your script
COPY get_YouTubeTranscript.py /scripts/get_transcript.py

USER node
