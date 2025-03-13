# This is a relatively lightweight chromium alpine image, so selenium has a browser to interface with
FROM zenika/alpine-chrome

# For use in the python script, to tell if it was launched in a docker container or in a test environment
ENV DOCKERIZED=1
# Allow python to print to the console from within docker container
ENV PYTHONBUFFERED=1

# Project files are located in src
COPY src /src
COPY requirements.txt .

# Need permissions for apk
USER root

# Get necessary python packages and install
RUN apk update && apk add --no-cache python3 py3-pip
RUN python3 -m venv /venv
RUN /venv/bin/pip install -r requirements.txt

# Install chromedriver using apk. Originally tried to manually download and unzip but ran into issues
RUN apk add --no-cache chromium-chromedriver

# Switch user back to chrome, as originally set by the parent image
USER chrome

# Override the parent image entrypoint, which causes issues with multiple chromium instances
# Also enters venv so python can run properly
ENTRYPOINT ["/venv/bin/python"] 

# Launch the selenium script
CMD ["/src/main.py"]