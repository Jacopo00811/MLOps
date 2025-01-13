# Base image
FROM python:3.11-slim

# Install Python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*
# Copy relevant files
COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY src/test_project/ test_project/
COPY data/ data/

# Set the working directory in our container and add commands that install the dependencies
WORKDIR /
# After the first build change to the other line to speed up process
RUN pip install -r requirements.txt --no-cache-dir
#RUN --mount=type=cache,target=~/pip/.cache pip install -r requirements.txt --no-cache-dir
RUN pip install . --no-deps --no-cache-dir

# Set the entrypoint
ENTRYPOINT ["python", "-u", "test_project/train.py"]