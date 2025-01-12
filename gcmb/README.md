## Finance Data

This project contains various indexes and currencies

```python
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
    Symbol("USD/EUR", "EURUSD=X", "Exchange rate between the United States Dollar and the Euro.", "currency"),
    Symbol("USD/JPY", "USDJPY=X", "Exchange rate between the United States Dollar and the Japanese Yen.", "currency"),
    Symbol("USD/GBP", "GBPUSD=X", "Exchange rate between the United States Dollar and the British Pound Sterling.", "currency"),
    Symbol("USD/AUD", "AUDUSD=X", "Exchange rate between the United States Dollar and the Australian Dollar.", "currency"),
    Symbol("USD/CAD", "USDCAD=X", "Exchange rate between the United States Dollar and the Canadian Dollar.", "currency"),
    Symbol("USD/CHF", "USDCHF=X", "Exchange rate between the United States Dollar and the Swiss Franc.", "currency"),
    Symbol("USD/CNY", "USDCNY=X", "Exchange rate between the United States Dollar and the Chinese Yuan.", "currency"),
    Symbol("USD/HKD", "USDHKD=X", "Exchange rate between the United States Dollar and the Hong Kong Dollar.", "currency"),
    Symbol("USD/INR", "USDINR=X", "Exchange rate between the United States Dollar and the Indian Rupee.", "currency"),
    Symbol("USD/SGD", "USDSGD=X", "Exchange rate between the United States Dollar and the Singapore Dollar.", "currency"),
    Symbol("USD/NZD", "NZDUSD=X", "Exchange rate between the United States Dollar and the New Zealand Dollar.", "currency"),
    Symbol("USD/KRW", "USDKRW=X", "Exchange rate between the United States Dollar and the South Korean Won.", "currency"),
    Symbol("USD/ZAR", "USDZAR=X", "Exchange rate between the United States Dollar and the South African Rand.", "currency"),
    Symbol("USD/SEK", "USDSEK=X", "Exchange rate between the United States Dollar and the Swedish Krona.", "currency"),
    Symbol("USD/NOK", "USDNOK=X", "Exchange rate between the United States Dollar and the Norwegian Krone.", "currency"),
    Symbol("USD/MXN", "USDMXN=X", "Exchange rate between the United States Dollar and the Mexican Peso.", "currency"),
    Symbol("USD/BRL", "USDBRL=X", "Exchange rate between the United States Dollar and the Brazilian Real.", "currency"),
    Symbol("USD/RUB", "USDRUB=X", "Exchange rate between the United States Dollar and the Russian Ruble.", "currency"),
    Symbol("USD/TRY", "USDTRY=X", "Exchange rate between the United States Dollar and the Turkish Lira.", "currency"),
    Symbol("EUR/USD", "EURUSD=X", "Exchange rate between the Euro and the United States Dollar.", "currency"),
    Symbol("EUR/JPY", "EURJPY=X", "Exchange rate between the Euro and the Japanese Yen.", "currency"),
    Symbol("EUR/GBP", "EURGBP=X", "Exchange rate between the Euro and the British Pound Sterling.", "currency"),
    Symbol("EUR/AUD", "EURAUD=X", "Exchange rate between the Euro and the Australian Dollar.", "currency"),
    Symbol("EUR/CAD", "EURCAD=X", "Exchange rate between the Euro and the Canadian Dollar.", "currency"),
    Symbol("EUR/CHF", "EURCHF=X", "Exchange rate between the Euro and the Swiss Franc.", "currency"),
    Symbol("EUR/CNY", "EURCNY=X", "Exchange rate between the Euro and the Chinese Yuan.", "currency"),
    Symbol("EUR/HKD", "EURHKD=X", "Exchange rate between the Euro and the Hong Kong Dollar.", "currency"),
    Symbol("EUR/INR", "EURINR=X", "Exchange rate between the Euro and the Indian Rupee.", "currency"),
    Symbol("EUR/SGD", "EURSGD=X", "Exchange rate between the Euro and the Singapore Dollar.", "currency"),
    Symbol("EUR/NZD", "EURNZD=X", "Exchange rate between the Euro and the New Zealand Dollar.", "currency"),
    Symbol("EUR/KRW", "EURKRW=X", "Exchange rate between the Euro and the South Korean Won.", "currency"),
    Symbol("EUR/ZAR", "EURZAR=X", "Exchange rate between the Euro and the South African Rand.", "currency"),
    Symbol("EUR/SEK", "EURSEK=X", "Exchange rate between the Euro and the Swedish Krona.", "currency"),
    Symbol("EUR/NOK", "EURNOK=X", "Exchange rate between the Euro and the Norwegian Krone.", "currency"),
    Symbol("EUR/MXN", "EURMXN=X", "Exchange rate between the Euro and the Mexican Peso.", "currency"),
    Symbol("EUR/BRL", "EURBRL=X", "Exchange rate between the Euro and the Brazilian Real.", "currency"),
    Symbol("EUR/RUB", "EURRUB=X", "Exchange rate between the Euro and the Russian Ruble.", "currency"),
    Symbol("EUR/TRY", "EURTRY=X", "Exchange rate between the Euro and the Turkish Lira.", "currency"),
    Symbol("BTC/USD", "BTC-USD", "Exchange rate between Bitcoin and the United States Dollar.", "currency"),
    Symbol("BTC/EUR", "BTC-EUR", "Exchange rate between Bitcoin and the Euro.", "currency"),
]
```

### Currencies against EURO

* USD: <Topic topic="finance/stock-exchange/currency/EURUSD=x" /> Euro
* JPY: <Topic topic="finance/stock-exchange/currency/EURJPY=x" /> Euro
* GBP: <Topic topic="finance/stock-exchange/currency/EURGBP=x" /> Euro
* AUD: <Topic topic="finance/stock-exchange/currency/EURAUD=x" /> Euro
* CAD: <Topic topic="finance/stock-exchange/currency/EURCAD=x" /> Euro
* CHF: <Topic topic="finance/stock-exchange/currency/EURCHF=x" /> Euro
* CNY: <Topic topic="finance/stock-exchange/currency/EURCNY=x" /> Euro
* HKD: <Topic topic="finance/stock-exchange/currency/EURHKD=x" /> Euro
* INR: <Topic topic="finance/stock-exchange/currency/EURINR=x" /> Euro
* SGD: <Topic topic="finance/stock-exchange/currency/EURSGD=x" /> Euro
* NZD: <Topic topic="finance/stock-exchange/currency/EURNZD=x" /> Euro
* KRW: <Topic topic="finance/stock-exchange/currency/EURKRW=x" /> Euro
* ZAR: <Topic topic="finance/stock-exchange/currency/EURZAR=x" /> Euro
* SEK: <Topic topic="finance/stock-exchange/currency/EURSEK=x" /> Euro
* NOK: <Topic topic="finance/stock-exchange/currency/EURNOK=x" /> Euro
* MXN: <Topic topic="finance/stock-exchange/currency/EURMXN=x" /> Euro
* BRL: <Topic topic="finance/stock-exchange/currency/EURBRL=x" /> Euro
* RUB: <Topic topic="finance/stock-exchange/currency/EURRUB=x" /> Euro
* TRY: <Topic topic="finance/stock-exchange/currency/EURTRY=x" /> Euro

### Currency against USD

TODO

### Indices

* Germany: DAX: <Topic topic="finance/stock-exchange/index/^GDAXI" /> Points
* Australia: S&P/ASX All Ordinaries: <Topic topic="finance/stock-exchange/index/^AORD" /> Points

TODO: Finish
