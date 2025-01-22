from dotenv import load_dotenv
load_dotenv()

import json
import yliveticker
import paho.mqtt.client as mqtt
import os
import logging
import sys
from symbols import all_symbols, all_symbols_by_identifier


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
            mqtt_publish(mqtt_client, symbol.topic(), price)
        except Exception as e:
            logging.error(f"Error processing message: {e}")

    yliveticker.YLiveTicker(on_ticker=on_new_msg, ticker_names=[s.yahoo_identifier for s in all_symbols])

    mqtt_client.loop_forever()


if __name__ == '__main__':
    main()
