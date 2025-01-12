FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl
 
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh
 
COPY pyproject.toml /pyproject.toml
COPY uv.lock /uv.lock
 
RUN /root/.local/bin/uv sync --frozen
 
COPY main.py /main.py

CMD ["/root/.local/bin/uv", "run", "main.py"]
