# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_PHONE = "Your Phone Number" # must be start +/country code/ +1XXXXXXXXX
TWILIO_PHONE = "Your twilio number" # +1XXXXXXXXXXX

ALPHA_VANTAGE_API_KEY = "your api key"
NEWS_ORG_API_KEY = "your api key"
TWILIO_AUTH_TOKEN = "your auth token"
TWILIO_ACCOUNT_SID = "your acount sid"
ALPHA_URL = "api endpoint for alpha vantage"
NEWS_API_URL = "api endpoint for news api"
# Imports
import requests
from twilio.rest import Client

# --- PARAMS ---
alpha_parameters = {
    "apikey": ALPHA_VANTAGE_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_ORG_API_KEY,
    "pageSize": 3,
    "sortBy": "publishedAt",
    "language": "en",
}
# Functions
def send_sms_alerts(change_pct, articles):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    direction = "🔺" if change_pct > 0 else "🔻"
    header_msg = f"{STOCK}: {direction} {change_pct:.2f}%\nNews for {COMPANY_NAME}:"
    client.messages.create(body=header_msg, from_=TWILIO_PHONE, to=MY_PHONE)

    for a in articles[:3]:
        title = (a.get("title") or "").strip()
        desc = (a.get("description") or "").strip()
        body = f"{title}\n{desc}"
        client.messages.create(body=body[:1500], from_=TWILIO_PHONE, to=MY_PHONE)

# --- STEP 1: STOCK DATA ---
stock_data = requests.get(url=ALPHA_URL, params=alpha_parameters)
stock_data.raise_for_status()
alpha_data = stock_data.json()

time_series = alpha_data["Time Series (Daily)"]
dates = sorted(time_series.keys(), reverse=True)
yesterday, day_before = dates[0], dates[1]

close_yesterday = float(time_series[yesterday]["4. close"])
close_day_before = float(time_series[day_before]["4. close"])

change_pct = ((close_yesterday - close_day_before) / close_day_before) * 100
print(f"{yesterday} close: {close_yesterday}")
print(f"{day_before} close: {close_day_before}")
print(f"Change: {change_pct:.2f}%")

# --- STEP 2 + 3: NEWS + SMS ---
if abs(change_pct) >= 5:
    r = requests.get(url=NEWS_API_URL, params=news_parameters)
    r.raise_for_status()
    articles = r.json()["articles"]

    # print (debug)
    for a in articles:
        print(a.get("title"))
        print(a.get("description"))
        print("---")

    # ✅ Send SMS alerts
    send_sms_alerts(change_pct, articles)

else:
    print("No major change")

