# FinancialMarkets_ProgressBars

> A pandas/tkinkter based programme using ranges (derived from price/volume/volatility) and live closing price metrics for 11 core financial instruments.

> A significant portion of the programme includes object orientated programming. Sections are displayed with a brief header to summarise the goal of the code below.

> Manual inputs of proprietary price range data (upper/lower daily price bands) are inputted into an excel file. This file has several tabs that are used outside the scope of this programme as well (also used for price/volume repository).

> Daily closing prices from several cross-asset classes are extracted using yfinance and are placed into a dataframe. 

> A specific time clamp is used to pinpoint the previous day's closing price irrespective of when the programme is executed (using datetime, timedelta and strftime).

> The specific price is extracted from the dataframe & expressed to 2 decimal places using the function 'extract_price'.

> Progress bar data is then calculated using the function 'bar'. The closing price level is calculated relative to the ranges and expressed as a progress bar (in percentage terms). This value is defined as 'ProgressPCT'. Objects are then created using this function to define all percentage levels (e.g. 'DAX_PCT')

> Tkinkter is then used to display these objects in progress bars. The 'Labels' function helps the viewer to assess what bars correspond to the financial instrument (green used for bullish trends/red used for bearish/down-trends).

> The programme is executed every morning where the user can swiftly assess the position of the closing price relative to both low and high parameters. It enables the viewer to save time and immediately access a visual representation of the previous day of trading in the financial markets.
