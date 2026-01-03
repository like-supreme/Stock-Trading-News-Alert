# Stock-Trading-News-Alert
A Python application that monitors daily stock price changes using Alpha Vantage, fetches related news with NewsAPI, and sends SMS alerts via Twilio when significant price movements occur.

# 📈 Stock News Alert System

A Python-based alert system that monitors daily stock price movements and notifies the user with relevant news articles via SMS when a significant change occurs.

---

## 🚀 Project Overview

This project tracks a selected stock's daily closing prices using the **Alpha Vantage API**.  
If the stock price changes by **5% or more** compared to the previous trading day, the system:

1. Fetches the **latest 3 news articles** related to the company using **NewsAPI**
2. Sends **SMS alerts** containing:
   - The percentage change
   - News headlines and descriptions  
   via **Twilio**

---

## 🧠 How It Works

1. Retrieve daily stock data
2. Compare yesterday's closing price with the day before
3. Calculate percentage change
4. If the change ≥ ±5%:
   - Fetch latest news articles
   - Send separate SMS messages for each article

---

## 🛠 Technologies Used

- **Python**
- **Alpha Vantage API** – Stock market data
- **NewsAPI** – Financial news articles
- **Twilio API** – SMS notifications
- **Requests** – HTTP requests handling

---

## 📦 Installation

1. Clone the repository:
   git clone https://github.com/your-username/stock-news-alert-system.git
   cd stock-news-alert-system

   pip install requests twilio

   For security reasons, API keys and sensitive information should not be hardcoded.

Create a .env file (not included in the repo):

ALPHA_VANTAGE_API_KEY=your_key_here
NEWS_ORG_API_KEY=your_key_here
TWILIO_ACCOUNT_SID=your_sid_here
TWILIO_AUTH_TOKEN=your_token_here
MY_PHONE=+1XXXXXXXXXX
TWILIO_PHONE=+1XXXXXXXXXX

Inside the code, configure the stock and company:

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

📲 Example Output
TSLA: 🔻 -5.42%
News for Tesla Inc:
• Tesla stock tumbles amid market uncertainty
• Investors react to earnings report
• Analysts revise price targets

⚠️ Notes

Alpha Vantage free tier has request limits

Twilio trial accounts require phone number verification

SMS permissions must be enabled for your region in Twilio (Geo Permissions)

📌 Future Improvements

Email notifications as an alternative to SMS

Support for multiple stocks

Scheduled execution with cron or task scheduler

Web dashboard for visualization

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.














