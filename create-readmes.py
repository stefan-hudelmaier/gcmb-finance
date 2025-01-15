import os

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
    for topic in currency_topics:
        directory = f'gcmb/{topic}'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(f'{directory}/README.md', 'a') as f:
            topic_parts = topic.split('/')
            currency = topic_parts[1]
            base_currency = topic_parts[2]
            f.write(f'## {topic_parts[1]}\n\n')
            f.write(f'This value of this topic is the price of one {currency} in {base_currency}.\n\n')
            f.write(f'## Current Value\n\n')
            f.write(f'1 {currency} = <Topic topic="{base_topic}/{topic}" decimals="3" unit="{base_currency}"/>\n\n')
