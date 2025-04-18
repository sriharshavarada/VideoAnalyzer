FROM n8nio/n8n

USER root

# Install Python + pip + build dependencies
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
  openssl-dev

# Install YouTube Transcript API
RUN pip3 install youtube-transcript-api

# Copy your script
COPY get_YouTubeTranscript.py /scripts/get_transcript.py

USER node
