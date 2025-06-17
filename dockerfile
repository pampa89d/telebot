FROM python:3.9-slim

ENV TOKEN = MY_TOKEN

COPY . . 

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
