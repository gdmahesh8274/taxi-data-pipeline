FROM python:3.14-slim
WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY main.py inspect_data.py query_data.py run_pipeline.py ./
CMD ["python", "run_pipeline.py"] 