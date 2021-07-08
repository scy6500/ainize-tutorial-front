FROM ubuntu:latest

WORKDIR /app

RUN pip3 install streamlit requests

COPY . .

CMD ["streamlit", "run", "app.py"]