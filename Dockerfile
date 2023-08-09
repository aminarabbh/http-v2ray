FROM ubuntu:latest
COPY . .
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    iputils-ping \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
USER root
ENTRYPOINT ["/bin/bash", "/jj.sh"]
