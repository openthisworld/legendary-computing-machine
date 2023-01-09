FROM python:3

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY generate_image.py .

ENV OPENAI_API_KEY "{{ secrets.API_KEY }}"

CMD ["python", "generate_image.py", "--prompt", "$PROMPT"]