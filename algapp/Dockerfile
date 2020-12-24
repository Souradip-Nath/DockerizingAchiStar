from python:3.8.7-buster

WORKDIR /home/souradipnathpwc/FinalProject/DockerizingAchiStar/algapp

COPY req.txt .
RUN pip install -r req.txt

COPY .  /home/souradipnathpwc/FinalProject/DockerizingAchiStar/algapp/

CMD [ "python","lineq.py" ]
