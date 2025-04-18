FROM n8nio/n8n

# Install Python and pip
USER root
RUN apt-get update && apt-get install -y python3 python3-pip

# Install YouTube Transcript API
RUN pip3 install youtube-transcript-api

# Copy your script into the container
COPY get_YouTubeTranscript.py /scripts/get_transcript.py

# Back to node user
USER node
