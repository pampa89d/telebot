FROM python:3.9-slim
ENV TOKEN='7801747532:AAExe2yV88JocFiz8cTMzYRbBeen4KFJ65I'
COPY . . 
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]
