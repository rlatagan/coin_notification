# this is the structure of the data being sent to use from the Coinmarketcap
# so it's a dictionary, and inside of it is 'data' which contains a list of dictionaries, i think
dict_struct = {'status': {'timestamp': '2022-01-14T07:41:58.905Z', 'error_code': 0},
               'data': [{
                   'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC'}, {
                   'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH'}, {
                   'id': 825, 'name': 'Tether', 'symbol': 'USDT'}]}

# this asks the user for input, and once again, it's just for testing
coin_input = input("Provide coin symbol (separate with comma for multiple coins): ")

# this will turn the input to an array
chosen_coin = coin_input.split(', ')
print(chosen_coin)

# this will be the final output
output_dict = {}

# we need the value of 'data' <-- the key
for coin_info in dict_struct['data']:

    for coin in chosen_coin:
        # for every dictionary in the list, the 'symbol' key will be compared to the coin
        if coin == coin_info['symbol']:

            # this is to insert the info to the dictionary we initially created earlier
            output_dict[coin] = coin_info['id']

print(output_dict)