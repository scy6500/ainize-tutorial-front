FROM python:3.8.13

WORKDIR /app

RUN pip install streamlit requests

COPY . .

CMD ["streamlit", "run", "app.py"]
