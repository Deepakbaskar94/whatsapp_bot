from flask import Flask, request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
  
  
app = Flask(__name__)
  
@app.route("/", methods=["POST"])
  
# chatbot logic
def bot():
  
    # user input
    user_msg = request.values.get('Body', '').lower()
  
    # creating object of MessagingResponse
    response = MessagingResponse()
  
    # User Query
    q = user_msg
  
    # list to store urls
    result = []
  
    # searching and storing 
    for i in search(q, num=10, stop=10, pause=2):
    #googlesearch.search(str: q, int: num_results=10, str: lang="en")-> list
    #googlesearch.search(str: q, int:num_results=6, str: lang="en"):
        result.append(i)
  
    # displaying result
    msg = response.message(f"--- Result for '{user_msg}' are  ---")
  
    for i in range(0,8):
        msg = response.message(result[i])
    # msg = response.message(result[1])
    # msg = response.message(result[2])
    # msg = response.message(result[3])
    # msg = response.message(result[4])
  
    return str(response)
  
  
if __name__ == "__main__":
    app.run()