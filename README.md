# EasySummary
Simple summarization algorithm using xintesis to publish the services 

Require:
* xintesis 
* spaCy
* en_core_web_sm spaCy model
* selenium-requests
* behave


Installation steps:

- Clone ans install xintesis
     
      git clone https://github.com/J41R0/Xintesis.git
      cd Xintesis
      python3 setup.py install

- Install spaCy

      pip install -U spacy
      python -m spacy download en_core_web_sm

- Run service 

      python3 wsgi.py