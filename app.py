from flask import Flask,request,jsonify
import requests
app = Flask(__name__)

@app.route('/',methods=["POST"])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_2Llp9PRGQ5yEgG64Nv5yTQEhguzFNsV8gWdQplm7"
    response = requests.get(url)
    response = response.json()
    response = response['data']
    final_amount = response[source_currency]*amount*response[target_currency]
    final_amount = round(final_amount,2)

    response_1 = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    return jsonify(response_1)


if __name__ == "__main__":
    app.run(debug=True)