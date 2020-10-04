FROM python

COPY . .

CMD [ "python", "./unitTest.py" ]
