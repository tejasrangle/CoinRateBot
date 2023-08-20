
# CoinRateBot

The Currency Conversion Chatbot is an intelligent virtual assistant designed to facilitate real-time currency conversion for users. Built using Dialogflow, this chatbot allows users to interact through natural language to get accurate and up-to-date currency conversion rates and perform currency conversions effortlessly.

## Demo
https://github.com/tejasrangle/CoinRateBot/assets/110970662/ad095be0-bb2b-41f0-a567-8c6b0d300201

## Chatbot Architecture

Here's the architecture for your Currency Conversion Chatbot using Dialogflow and Telegram:
1. User Interaction:
- Users interact with the chatbot on the Telegram platform by sending messages like "Convert 100 USD to EUR" or "What's the exchange rate for USD to GBP?"

2. Dialogflow:
- Intents: Dialogflow recognizes user intents such as "CurrencyConversion" based on the user's input. It also extracts entities like source currency, target currency, and amount from the user's query.
- Contexts: Contexts help maintain conversation context, ensuring a smooth flow of conversation, and allowing the chatbot to remember previous user inputs.

3. Fulfillment:
- Webhook: When an intent is triggered, Dialogflow sends a webhook request to your Flask application.
4. Flask Application:
- Your Flask application acts as the fulfillment endpoint.
- It receives the webhook request from Dialogflow containing the user's intent, entities, and context.
- The application uses the received data to perform currency conversion by interacting with external currency exchange APIs.
- It calculates the converted amount and prepares a response.
5. External APIs:
- Currency Exchange API: Your Flask application interacts with external currency exchange APIs to fetch real-time conversion rates.
6. Flask Application Response:
- Once the Flask application calculates the converted amount, it sends a response back to Dialogflow in JSON format.
7. Dialogflow Response:
- Dialogflow processes the response from the Flask application.
- It generates a reply to the user based on the fulfillment response.
- This reply might include the converted amount, a confirmation message, or an error message.
8. Telegram Integration:
- Dialogflow is integrated with the Telegram platform.
- When Dialogflow generates a response, it's sent back to the user on Telegram as a reply to the user's original message.


## Feedback

If you have any feedback, please reach out to us at tejasrangle31@gmail.com

