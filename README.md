# FinancialMarkets_ProgressBars

A data analysis and GUI (progress-bar) based program using ranges (derived from price/volume/volatility) and live closing price data. 
The purpose of the project was to clearly present up-to-date financial market information in conjunction with self-generated data (proprietary price ranges).The user can swiftly access a visual representation of where closing price data is located relative to the low/top range parameters.


## Technologies

- Language: Python 3.8.3

- Editor: PyCharm

- Libraries:
    - Yfinance
    - Datetime
    - Tkinkter
    - Pandas


## Setup

The excel file containing the ranges is required to be stored on the user’s directory. This file has several tabs that are used outside the scope of this program as well. This is not attached, however a screenshot of the program GUI is included below.


## Walkthrough

<b>Time Clamp:</b>

A final time point is defined using ‘timedelta’ and ‘strftime’. This enables the user to access up-to-date data whenever the program is executed.


<b>Ranges:</b>

Price ranges from a pre-existing excel file are accessed using pandas. Each low/high range parameter for each financial instrument are placed into objects to be used in later functions. Eleven financial markets are used (22 objects). 


<b>Time Clamp:</b>

A final time point is defined using ‘timedelta’ and ‘strftime’. This enables the user to access up-to-date data whenever the program is executed.


<b>Dataframe:</b>

Daily closing prices from 11 asset classes are extracted using yfinance and are placed into a dataframe. The adjusted closing prices are extracted (‘extract_price’ function) using ‘iloc’ and rounded to 2 decimal places.

<b>Progress-Bar Data:</b>

The ‘bar’ function is used to define the gap between the ranges and calculate where the price is located relative to the range parameters. This distance is expressed as a percentage (object = ‘ProgressPCT’). The objects to be used in tkinkter are then defined (i.e. EUR_PCT).

 <b>GUI:</b>
 
- A tkinkter window is defined and the in-built property of progress-bars are configured. The progress-bar ‘values’ are then connected with the PCT objects mentioned above (‘PCT_Fill’ function).
 - Labels and progress-bars are designed. Red bars are used for current bearish (down) trends and green bars are used for current bullish (up) trends. The ‘Finalise’ list is iterated over in a ‘for’ loop to pack every financial instrument into the window.
- The user is able to gain a visual insight into the rate of change of price movements and the relationship of this with the dynamic ranges provided. This is used to aid investing/trading decision making.

## Screenshot

![ProgressBar Example](https://user-images.githubusercontent.com/72507931/99262531-06003300-2816-11eb-9b11-44f62ed1047f.JPG)


## Status

Project completed.
