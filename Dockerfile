FROM python:3

RUN pip install reportlab

COPY ./statics/ /statics/
COPY ./tests /tests

CMD python -m unittest tests.test_sample_pdf
