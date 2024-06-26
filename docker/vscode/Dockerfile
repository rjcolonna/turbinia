# We take the latest Turbinia worker release as a base image to make sure dependencies are already installed
FROM us-docker.pkg.dev/osdfir-registry/turbinia/release/turbinia-worker-dev:latest

USER root

# Cleanup installed turbinia from base image
RUN pip uninstall -y turbinia
RUN if [ -f /usr/local/bin/turbiniactl ] ; then rm /usr/local/bin/turbiniactl ; fi

# Create /evidence and /tmp/turbinia-mounts folders (used in local stack configuration)
RUN mkdir /evidence && chmod 777 /evidence
RUN mkdir -p /tmp/turbinia-mounts && chmod 777 /tmp/turbinia-mounts

# Run apt-update before installing any packages
RUN apt-get update -y

# Install pylint, yapf and test tools
RUN pip install pylint yapf
RUN pip install mock nose coverage tox

# Install redis server
RUN apt-get -y install redis-server curl vim
# disable IPv6 in redis configuration
RUN sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

# Install Google Cloud SDK
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - \
  && apt-get update -y \
  && apt-get install google-cloud-sdk -y

# Install NodeJS for frontend development
RUN curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get update && apt-get install -y --no-install-recommends \
  nodejs \
  && rm -rf /var/lib/apt/lists/*

# Insert dummy command to override base image CMD
CMD ["/usr/bin/ps"]
