# pip install tda-api
# pip install --upgrade tda-api
# pip install -r requirements.txt

from tda import auth, client
import json, config, datetime

import os
path = os.getcwd()
CHROME_DRIVER = path + '/chromedriver.exe'


try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path=CHROME_DRIVER) as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

# r = c.get_price_history('AAPL',
#         period_type=client.Client.PriceHistory.PeriodType.YEAR,
#         period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#         frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#         frequency=client.Client.PriceHistory.Frequency.DAILY)
# assert r.status_code == 200, r.raise_for_status()
# print(json.dumps(r.json(), indent=4))

# response = c.get_quote ('BA')
# print(response.json())

# response = c.search_instruments(['AAPL', 'BA'], c.Instrument.Projection.FUNDAMENTAL)
# print(json.dumps(response.json(), indent=4))

# response = c.get_option_chain('APPL')
# print(json.dumps(response.json(), indent=4))

# Show all call options for AAPL
# response = c.get_option_chain('APPL', contract_type=c.Options.ContractType.CALL)
# print(json.dumps(response.json(), indent=4))

# All options for AAPL where the strike is 300
# response = c.get_option_chain('APPL', contract_type=c.Options.ContractType.ALL, strike=300 )
# print(json.dumps(response.json(), indent=4))

# All options for a specific strike and date range
start_date = datetime.datetime.strptime('2021-09-10', '%Y-%m-%d').date()
end_date = datetime.datetime.strptime('2021-12-10', '%Y-%m-%d').date()
response = c.get_option_chain('AAPL', contract_type=c.Options.ContractType.ALL, strike=146, from_date=start_date, to_date=end_date )
print(json.dumps(response.json(), indent=4))


############################  ORDER EXECUTION #####################################################################################
# from tda.orders.equities import equity_buy_limit
# from tda.orders.common import Duration, Session

# client.place_order(
#     1000,  # account_id
#     equity_buy_limit('GOOG', 1, 1250.0)
#         .set_duration(Duration.GOOD_TILL_CANCEL)
#         .set_session(Session.SEAMLESS)
#         .build())
