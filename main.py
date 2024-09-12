import os
import requests
import re
from dotenv import load_dotenv
import time
load_dotenv()
from cloudflare import Cloudflare

def get_ip_addr():
    response = requests.get("https://cloudflare.com/cdn-cgi/trace")
    ip_match = re.search(r"ip=([^\n\r]+)", response.text)
    return ip_match.group(1)

client = Cloudflare(
    # This is the default and can be omitted
    # api_email=os.environ.get("CLOUDFLARE_EMAIL"),
    # This is the default and can be omitted
    api_token=os.environ.get("CLOUDFLARE_API_TOKEN"),
)

ZONE_ID = os.environ.get("CLOUDFLARE_ZONE_ID")
DDNS_RECORD_NAME = os.environ.get("DDNS_RECORD_NAME")
# DEFAULT 5 seconds
DDNS_REFRESH_INTERVAL = int(os.environ.get("DDNS_REFRESH_INTERVAL")) if os.environ.get("DDNS_REFRESH_INTERVAL") else 5

zone = client.zones.get(zone_id=ZONE_ID)
RECORD_NAME=f"{DDNS_RECORD_NAME}.{zone.name}".lower()
IP_ADDR = os.environ.get("IP_ADDR") if os.environ.get("IP_ADDR") else get_ip_addr()

dns_records = client.dns.records.list(zone_id=ZONE_ID)
dns_record = None

for record in dns_records:
    if record.name == RECORD_NAME:
        dns_record = record

while True:
    if dns_record is None:
        client.dns.records.create(
            zone_id=ZONE_ID,
            name=RECORD_NAME,
            type="A",
            content=IP_ADDR,
            proxied=False
        )
    else:
        client.dns.records.edit(
            zone_id=ZONE_ID,
            dns_record_id=dns_record.id,
            name=RECORD_NAME,
            type="A",
            content=IP_ADDR,
            proxied=False
        )
    print(f"{RECORD_NAME} -> {IP_ADDR}")
    time.sleep(DDNS_REFRESH_INTERVAL)