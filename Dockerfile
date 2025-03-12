# This is a "lightweight" chromium image, which I'm using as a basis for this project
FROM zenika/alpine-chrome

# All the code and requirements.txt is in src
COPY src /src

# Need permissions for apk
USER root
RUN apk update && apk add --no-cache python3 py3-pip

RUN python3 -m venv /venv

RUN /venv/bin/pip install -r /src/requirements.txt

# Install chromedriver using apk. Originally tried to wget and unzip but ran into issues
RUN apk add --no-cache chromium-chromedriver

# Make sure the chromedriver is accessible
RUN which chromedriver
RUN ls -la /usr/bin/chromedriver

# Make sure the src directory is accessible
RUN chown -R chrome:chrome /src
RUN chmod -R 755 /src

# Switch back to chrome, was originally setup by the parent image
USER chrome

# Override the parent image entrypoint
ENTRYPOINT [] 

# Execute command as a string, so python can run in the venv
CMD ["/bin/sh", "-c", "cd /src && /venv/bin/python /src/main.py"]