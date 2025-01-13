from dotenv import load_dotenv
load_dotenv()

import json
import yliveticker
from dataclasses import dataclass
import paho.mqtt.client as mqtt
import os
import logging
import sys


broker = os.environ.get('MQTT_HOST', 'gcmb.io')
client_id = os.environ['MQTT_CLIENT_ID']
username = os.environ['MQTT_USERNAME']
password = os.environ['MQTT_PASSWORD']
port = 8883

log_level = os.environ.get('LOG_LEVEL', 'INFO')
print("Using log level", log_level)

logger = logging.getLogger()
logger.setLevel(log_level)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@dataclass
class Symbol:
    name: str
    yahoo_identifier: str
    description: str
    symbol_type: str


indices = [
    Symbol("DAX", "^GDAXI", "The DAX index represents 30 major German companies trading on the Frankfurt Stock Exchange.", "index"),
    Symbol("SP500", "^GSPC", "The S&P 500 index tracks 500 large-cap U.S. companies listed on the NYSE or NASDAQ.", "index"),
    Symbol("Nasdaq", "^IXIC", "The Nasdaq Composite index includes over 3,000 stocks listed on the Nasdaq Stock Market.", "index"),
    Symbol("Dow Jones", "^DJI", "The Dow Jones Industrial Average tracks 30 prominent U.S. companies.", "index"),
    Symbol("FTSE", "^FTSE", "The FTSE 100 index includes the top 100 companies listed on the London Stock Exchange.", "index"),
    Symbol("Nikkei", "^N225", "The Nikkei 225 index tracks 225 large, publicly-owned companies in Japan.", "index"),
    Symbol("CAC 40", "^FCHI", "The CAC 40 index represents 40 of the largest French companies traded on the Euronext Paris.", "index"),
    Symbol("Hang Seng", "^HSI", "The Hang Seng index includes the largest companies listed on the Hong Kong Stock Exchange.", "index"),
    Symbol("ASX 200", "^AXJO", "The ASX 200 index represents the top 200 stocks listed on the Australian Securities Exchange.", "index"),
    Symbol("KOSPI", "^KS11", "The KOSPI index tracks all common stocks traded on the Korea Exchange.", "index"),
    Symbol("Shanghai Composite", "000001.SS", "The Shanghai Composite index includes all stocks traded on the Shanghai Stock Exchange.", "index"),
    Symbol("BSE Sensex", "^BSESN", "The BSE Sensex index represents 30 well-established and financially sound companies listed on the Bombay Stock Exchange.", "index"),
    Symbol("TSX", "^GSPTSE", "The TSX Composite index represents the performance of the Toronto Stock Exchange.", "index"),
    Symbol("Euronext 100", "^N100", "The Euronext 100 index comprises the top 100 blue-chip stocks listed on the Euronext exchange.", "index"),
    Symbol("Russell 2000", "^RUT", "The Russell 2000 index represents 2,000 small-cap companies in the U.S. market.", "index"),
    Symbol("Euro Stoxx 50", "^STOXX50E", "The Euro Stoxx 50 index tracks the 50 largest companies in the Eurozone.", "index"),
    Symbol("Ibovespa", "^BVSP", "The Ibovespa index is the benchmark index of the São Paulo Stock Exchange, representing the performance of the top companies in Brazil.", "index"),
    Symbol("S&P/ASX All Ordinaries", "^AORD", "The S&P/ASX All Ordinaries index represents the performance of the Australian stock market.", "index"),
    Symbol("MSCI World", "^MSCIWO", "The MSCI World index tracks large and mid-cap companies across 23 developed markets worldwide.", "index"),
    Symbol("MSCI Emerging Markets", "^MSCIEF", "The MSCI Emerging Markets index represents large and mid-cap companies across 27 emerging markets.", "index"),
    Symbol("Kuala Lumpur Composite", "^KLSE", "The Kuala Lumpur Composite index tracks the performance of the 30 largest companies listed on the Bursa Malaysia.", "index"),
    Symbol("S&P BSE 500", "^BSE500", "The S&P BSE 500 index tracks the performance of the top 500 companies listed on the Bombay Stock Exchange.", "index"),
    Symbol("OMX Stockholm 30", "^OMX", "The OMX Stockholm 30 index represents the 30 most traded stocks on the Stockholm Stock Exchange.", "index"),
    Symbol("Tadawul All Share Index", "^TASI", "The Tadawul All Share Index is the benchmark index for the Saudi Stock Exchange.", "index"),
    Symbol("FTSE MIB", "FTSEMIB.MI", "The FTSE MIB index is the benchmark index for the Borsa Italiana, tracking the 40 most significant companies listed in Italy.", "index")
]

currencies = [
    Symbol("USD/EUR", "USDEUR=X", "Exchange rate between the Euro and the United States Dollar.", "currency"),
    Symbol("JPY/EUR", "JPYEUR=X", "Exchange rate between the Euro and the Japanese Yen.", "currency"),
    Symbol("GBP/EUR", "GBPEUR=X", "Exchange rate between the Euro and the British Pound Sterling.", "currency"),
    Symbol("AUD/EUR", "AUDEUR=X", "Exchange rate between the Euro and the Australian Dollar.", "currency"),
    Symbol("CAD/EUR", "CADEUR=X", "Exchange rate between the Euro and the Canadian Dollar.", "currency"),
    Symbol("CHF/EUR", "CHFEUR=X", "Exchange rate between the Euro and the Swiss Franc.", "currency"),
    Symbol("CNY/EUR", "CNYEUR=X", "Exchange rate between the Euro and the Chinese Yuan.", "currency"),
    Symbol("HKD/EUR", "HKDEUR=X", "Exchange rate between the Euro and the Hong Kong Dollar.", "currency"),
    Symbol("INR/EUR", "INREUR=X", "Exchange rate between the Euro and the Indian Rupee.", "currency"),
    Symbol("SGD/EUR", "SGDEUR=X", "Exchange rate between the Euro and the Singapore Dollar.", "currency"),
    Symbol("NZD/EUR", "NZDEUR=X", "Exchange rate between the Euro and the New Zealand Dollar.", "currency"),
    Symbol("KRW/EUR", "KRWEUR=X", "Exchange rate between the Euro and the South Korean Won.", "currency"),
    Symbol("ZAR/EUR", "ZAREUR=X", "Exchange rate between the Euro and the South African Rand.", "currency"),
    Symbol("SEK/EUR", "SEKEUR=X", "Exchange rate between the Euro and the Swedish Krona.", "currency"),
    Symbol("NOK/EUR", "NOKEUR=X", "Exchange rate between the Euro and the Norwegian Krone.", "currency"),
    Symbol("MXN/EUR", "MXNEUR=X", "Exchange rate between the Euro and the Mexican Peso.", "currency"),
    Symbol("BRL/EUR", "BRLEUR=X", "Exchange rate between the Euro and the Brazilian Real.", "currency"),
    Symbol("RUB/EUR", "RUBEUR=X", "Exchange rate between the Euro and the Russian Ruble.", "currency"),
    Symbol("TRY/EUR", "TRYEUR=X", "Exchange rate between the Euro and the Turkish Lira.", "currency"),
    Symbol("EUR/USD", "EURUSD=X", "Exchange rate between the United States Dollar and the Euro.", "currency"),
    Symbol("JPY/USD", "JPYUSD=X", "Exchange rate between the United States Dollar and the Japanese Yen.", "currency"),
    Symbol("GBP/USD", "GBPUSD=X", "Exchange rate between the United States Dollar and the British Pound Sterling.", "currency"),
    Symbol("AUD/USD", "AUDUSD=X", "Exchange rate between the United States Dollar and the Australian Dollar.", "currency"),
    Symbol("CAD/USD", "CADUSD=X", "Exchange rate between the United States Dollar and the Canadian Dollar.", "currency"),
    Symbol("CHF/USD", "CHFUSD=X", "Exchange rate between the United States Dollar and the Swiss Franc.", "currency"),
    Symbol("CNY/USD", "CNYUSD=X", "Exchange rate between the United States Dollar and the Chinese Yuan.", "currency"),
    Symbol("HKD/USD", "HKDUSD=X", "Exchange rate between the United States Dollar and the Hong Kong Dollar.", "currency"),
    Symbol("INR/USD", "INRUSD=X", "Exchange rate between the United States Dollar and the Indian Rupee.", "currency"),
    Symbol("SGD/USD", "SGDUSD=X", "Exchange rate between the United States Dollar and the Singapore Dollar.", "currency"),
    Symbol("NZD/USD", "NZDUSD=X", "Exchange rate between the United States Dollar and the New Zealand Dollar.", "currency"),
    Symbol("KRW/USD", "KRWUSD=X", "Exchange rate between the United States Dollar and the South Korean Won.", "currency"),
    Symbol("ZAR/USD", "ZARUSD=X", "Exchange rate between the United States Dollar and the South African Rand.", "currency"),
    Symbol("SEK/USD", "SEKUSD=X", "Exchange rate between the United States Dollar and the Swedish Krona.", "currency"),
    Symbol("NOK/USD", "NOKUSD=X", "Exchange rate between the United States Dollar and the Norwegian Krone.", "currency"),
    Symbol("MXN/USD", "MXNUSD=X", "Exchange rate between the United States Dollar and the Mexican Peso.", "currency"),
    Symbol("BRL/USD", "BRLUSD=X", "Exchange rate between the United States Dollar and the Brazilian Real.", "currency"),
    Symbol("RUB/USD", "RUBUSD=X", "Exchange rate between the United States Dollar and the Russian Ruble.", "currency"),
    Symbol("TRY/USD", "TRYUSD=X", "Exchange rate between the United States Dollar and the Turkish Lira.", "currency"),
    Symbol("BTC/USD", "BTC-USD", "Exchange rate between Bitcoin and the United States Dollar.", "currency"),
    Symbol("BTC/EUR", "BTC-EUR", "Exchange rate between Bitcoin and the Euro.", "currency"),
]


all_symbols = indices + currencies
all_symbols_by_identifier = {s.yahoo_identifier: s for s in all_symbols}


def connect_mqtt():
    def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            logger.info("Connected to MQTT Broker")
        else:
            logger.error(f"Failed to connect, return code {rc}")

    mqtt_client = mqtt.Client(client_id=client_id,
                              callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.tls_set(ca_certs='/etc/ssl/certs/ca-certificates.crt')
    mqtt_client.username_pw_set(username, password)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = lambda client, userdata, disconnect_flags, reason_code, properties: logger.warning(
        f"Disconnected from MQTT Broker, return code {reason_code}")
    mqtt_client.connect(broker, port)
    return mqtt_client


def mqtt_publish(client, topic, msg):
    result = client.publish(topic, msg, retain=True)
    status = result.rc
    if status == 0:
        logger.debug(f"Sent '{msg}' to topic {topic}")
    else:
        logger.warning(f"Failed to send message to topic {topic}, reason: {status}")


def main():
    mqtt_client = connect_mqtt()

    def on_new_msg(ws, update):
        try:
            symbol_id = update['id']
            if not symbol_id in all_symbols_by_identifier:
                logger.warning(f"Unknown symbol: {symbol_id}")
                return
            symbol = all_symbols_by_identifier[symbol_id]
            price = update['price']
            if symbol.symbol_type == 'currency':
                # Currencies are published to e.g. finance/stock-exchange/currency/EUR/USD
                topic = f"finance/stock-exchange/currency/{symbol.name}"
            else:
                # Indices are publish to e.g. finance/stock-exchange/index/GDAXI (without the special character)
                symbol_topic = symbol.yahoo_identifier.replace('^', '')
                topic = f"finance/stock-exchange/index/{symbol_topic}"
            mqtt_publish(mqtt_client, topic, price)
        except Exception as e:
            logging.error(f"Error processing message: {e}")

    yliveticker.YLiveTicker(on_ticker=on_new_msg, ticker_names=[s.yahoo_identifier for s in all_symbols])

    mqtt_client.loop_forever()


if __name__ == '__main__':
    main()
