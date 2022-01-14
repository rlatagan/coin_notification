import requests
import time

'''
    api_key <-- can be retrieved from the Coinmarketcap site once you've made an account
    bot_token <-- from the Telegram BotFather, they will provide you with a token once you've created a bot
    chat_id <-- the chat id of the user you want the script to send the notifications to
    time_interval <-- the time in between api requests, 333 API REQUESTS CAN BE MADE PER DAY WITH COINMARKETCAP
    chosen_coin <-- coins that we want to receive notifications of (in str array form)
    output_dict <-- the output {'coin': price}
'''
# variables
api_key = '25531e84-9b6f-4602-85eb-6e0190523016'
bot_token = '5048534209:AAFXkVGZ3xH4k312U6GB-UxJc80_lpQmEZc'
chat_id = '5072212246'
time_interval = 10 * 60  # this is in seconds, so the script will make an API request every 10 minutes
chosen_coin = ['BTC', 'BNB', 'ETH']
output_dict = {}


# this function will retrieve the coin price
def get_coin_price():
    # this is the api endpoint to get the latest prices
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }

    # makes a request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()

    # then we get the prices of the coins we need, better explanation is in test2.py
    for coin_info in response_json['data']:
        for coin in chosen_coin:
            if coin == coin_info['symbol']:
                output_dict[coin] = coin_info['quote']['USD']['price']

    return output_dict


# this function sends a message through telegram
def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


# this function just edits output_dict
def format_output(output_dict):
    message = ''
    for key, value in output_dict.items():
        if not message:
            message = key + ': ' + str(value)
        else:
            message = message + "\n" + key + ': ' + str(value)

    return message


# this is the main function
def main():
    # TO INFINITY AND BEYOND, this is just an infinite loop
    while True:
        prices = get_coin_price()

        send_message(chat_id=chat_id, msg=f'{format_output(prices)}')

        # this is a timer, once time_interval has passed, the loop will continue
        time.sleep(time_interval)


if __name__ == '__main__':
    main()
