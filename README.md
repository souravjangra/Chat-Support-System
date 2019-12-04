# Chat-Support-System
Multiprocess chat support system where a minimal bot responds to a fixed set of text queries.

Requirements
Python 3.6 or greater

Following modules to be installed using pip:

pip install pipenv
after that install modules using pipenv from the given pipfile in the repository
using pipenv install

then run 
1.) pipenv shell
2.) uvicorn app:app --reload
3.) python app.py
4.) python client.py

after that visit http://127.0.0.1:8000/ and you'll get some hello world json response.
and http://127.0.0.1:8000/client-count for showing how many clients are connected to the server.
