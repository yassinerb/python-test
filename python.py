import os
from flask import flask
message=os.environ['MESSAGE']
app=flask (__name__)
@app.route('/')
def hello():
return 'our message is {}.\n'.format(message)
if __name__=="__main__":
app.run(host='0.0.0.0',port=5000)
