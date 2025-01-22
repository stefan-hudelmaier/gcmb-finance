import os

from symbols import all_symbols

base_topic = "finance/stock-exchange"

currency_topics = [
    "currency/USD/EUR",
    "currency/JPY/EUR",
    "currency/GBP/EUR",
    "currency/AUD/EUR",
    "currency/CAD/EUR",
    "currency/CHF/EUR",
    "currency/CNY/EUR",
    "currency/HKD/EUR",
    "currency/INR/EUR",
    "currency/SGD/EUR",
    "currency/NZD/EUR",
    "currency/KRW/EUR",
    "currency/ZAR/EUR",
    "currency/SEK/EUR",
    "currency/NOK/EUR",
    "currency/MXN/EUR",
    "currency/BRL/EUR",
    "currency/RUB/EUR",
    "currency/TRY/EUR",
    "currency/EUR/USD",
    "currency/JPY/USD",
    "currency/GBP/USD",
    "currency/AUD/USD",
    "currency/CAD/USD",
    "currency/CHF/USD",
    "currency/CNY/USD",
    "currency/HKD/USD",
    "currency/INR/USD",
    "currency/SGD/USD",
    "currency/NZD/USD",
    "currency/KRW/USD",
    "currency/ZAR/USD",
    "currency/SEK/USD",
    "currency/NOK/USD",
    "currency/MXN/USD",
    "currency/BRL/USD",
    "currency/RUB/USD",
    "currency/TRY/USD"
]

if __name__ == '__main__':
    for symbol in all_symbols:

        topic_parts = symbol.topic().split('/')
        print(topic_parts)
        relative_topic_parts = topic_parts[2:]
        relative_topic = '/'.join(relative_topic_parts)
        directory = f'gcmb/{relative_topic}'

        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(f'{directory}/README.md', 'w') as f:
            f.write(f'## {symbol.name}\n\n')
            f.write(f'{symbol.description}\n\n')
            f.write(f'## Current Value\n\n')
            if symbol.symbol_type == 'currency':
                currency = relative_topic_parts[1]
                base_currency = relative_topic_parts[2]
                f.write(f'1 {currency} = <Topic topic="{symbol.topic()}" decimals="3" unit="{base_currency}"/>\n\n')
            elif symbol.symbol_type == 'index':
                f.write(f'<Topic topic="{symbol.topic()}" decimals="2" unit="points"/>\n\n')

            f.write(f'## More information\n\n')
            f.write(f'More information can be found here: [{symbol.yahoo_identifier} on Yahoo Finance](https://finance.yahoo.com/quote/{symbol.yahoo_identifier}/)\n')

