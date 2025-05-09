from dotenv import load_dotenv
load_dotenv()

import yliveticker
import os
import logging
import sys
from symbols import all_symbols, all_symbols_by_identifier
import time
from gcmb_publisher import MqttPublisher
from threading import Thread

log_level = os.environ.get('LOG_LEVEL', 'INFO')
print("Using log level", log_level)

logger = logging.getLogger()
logger.setLevel(log_level)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

mqtt_publisher = MqttPublisher(enable_watchdog=True)

def on_websocket_close(ws, close_status, close_msg):
    logger.error(f"Websocket closed: {close_status} {close_msg}. Exiting.")
    # Let it crash
    sys.exit(1)


def on_websocket_error(ws, error):
    logger.error(f"Websocket error: {error}. Exiting")
    # Let it crash
    sys.exit(1)


def main():

    def on_new_msg(ws, update):
        try:
            symbol_id = update['id']
            if not symbol_id in all_symbols_by_identifier:
                logger.warning(f"Unknown symbol: {symbol_id}")
                return
            symbol = all_symbols_by_identifier[symbol_id]
            price = update['price']
            mqtt_publisher.send_msg(price, symbol.topic(), retain=True)

        except Exception as e:
            logging.error(f"Error processing message: {e}")


    yliveticker.YLiveTicker(
        ticker_names=[s.yahoo_identifier for s in all_symbols],
        on_ticker=on_new_msg, 
        on_close=on_websocket_close,
        on_error=on_websocket_error
    )


if __name__ == '__main__':
    main()
