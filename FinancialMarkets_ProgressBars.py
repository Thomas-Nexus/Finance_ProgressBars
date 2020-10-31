import pandas as pd
import yfinance as yf
from datetime import date, timedelta

#-----------------------------------------------------------------------------------------------------------------------
#ACCESS RANGE DATA

def ranges(extract):
    Instrument = pd.read_excel('RANGE DATA.xlsx')
    Low = Instrument.iloc[extract, 1]
    Top = Instrument.iloc[extract, 2]
    return Low, Top

VIXLE = ranges(1)[0]
VIXTE = ranges(1)[1]
USTLE = ranges(2)[0]
USTTE = ranges(2)[1]
DAXLE = ranges(3)[0]
DAXTE = ranges(3)[1]
DXYLE = ranges(4)[0]
DXYTE = ranges(4)[1]
EURLE = ranges(5)[0]
EURTE = ranges(5)[1]
RUTLE = ranges(6)[0]
RUTTE = ranges(6)[1]
NIKLE = ranges(7)[0]
NIKTE = ranges(7)[1]
GLDLE = ranges(8)[0]
GLDTE = ranges(8)[1]
SPYLE = ranges(9)[0]
SPYTE = ranges(9)[1]
YENLE = ranges(10)[0]
YENTE = ranges(10)[1]
OILLE = ranges(11)[0]
OILTE = ranges(11)[1]

#-----------------------------------------------------------------------------------------------------------------------
#DEFINE TIME SERIES

TimeClamp1 = date.today()
TimeClamp1.strftime('%Y-%m-%d')
TimeClamp2 = date.today() + timedelta(2)
TimeClamp2.strftime('%Y-%m-%d')

#------------------------------------------------------------------------------------------------------------------------
#EXTRACT PRICE DATA

def closingprice(code):
    Instrument = pd.DataFrame(yf.download(code, start=TimeClamp1, end=TimeClamp2)['Adj Close'])
    return Instrument

VIX_Price = closingprice('^VIX')
UST_Price = closingprice('^TNX')
DAX_Price = closingprice('^GDAXI')
DXY_Price = closingprice('DX=F')
EUR_Price = closingprice('EURUSD=X')
RUT_Price = closingprice('^RUT')
YEN_Price = closingprice('JPY=X')
OIL_Price = closingprice('CL=F')
NIK_Price = closingprice('^N225')
GLD_Price = closingprice('GC=F')
SPY_Price = closingprice('^GSPC')

#-----------------------------------------------------------------------------------------------------------------------
# EXTRACT PRICE FROM THE DF

def extract_price(closingDF):
    Num = closingDF['Adj Close']
    NumB = Num.iloc[0]
    NumC = NumB.astype(float)
    Num2 = round(NumC, 2)
    return Num2

VIX_Price_Extract = extract_price(VIX_Price)
UST_Price_Extract = extract_price(UST_Price)
DAX_Price_Extract = extract_price(DAX_Price)
DXY_Price_Extract = extract_price(DXY_Price)
EUR_Price_Extract = extract_price(EUR_Price)
RUT_Price_Extract = extract_price(RUT_Price)
YEN_Price_Extract = extract_price(YEN_Price)
OIL_Price_Extract = extract_price(OIL_Price)
NIK_Price_Extract = extract_price(NIK_Price)
GLD_Price_Extract = extract_price(GLD_Price)
SPY_Price_Extract = extract_price(SPY_Price)

#-----------------------------------------------------------------------------------------------------------------------
# FORMULATE PROGRESS BAR DATA

def bar(Low, Top, Price):
    GAP = Top - Low
    PriceFromL = Price - Low
    Progress = PriceFromL/GAP
    ProgressPCT = Progress * 100
    return ProgressPCT

VIX_PCT = bar(VIXLE, VIXTE, VIX_Price_Extract)
UST_PCT = bar(USTLE, USTTE, UST_Price_Extract)
DAX_PCT = bar(DAXLE, DAXTE, DAX_Price_Extract)
DXY_PCT = bar(DXYLE, DXYTE, DXY_Price_Extract)
EUR_PCT = bar(EURLE, EURTE, EUR_Price_Extract)
RUT_PCT = bar(RUTLE, RUTTE, RUT_Price_Extract)
YEN_PCT = bar(SPYLE, SPYTE, SPY_Price_Extract)
OIL_PCT = bar(OILLE, OILTE, OIL_Price_Extract)
NIK_PCT = bar(NIKLE, NIKTE, NIK_Price_Extract)
GLD_PCT = bar(GLDLE, GLDTE, GLD_Price_Extract)
SPY_PCT = bar(SPYLE, SPYTE, SPY_Price_Extract)

#-----------------------------------------------------------------------------------------------------------------------
# GUI

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('RANGES')
root.geometry('350x420')
root.configure(bg='black')
s = ttk.Style()
s.theme_use('classic')
s.configure("red.Horizontal.TProgressbar", troughcolor='white', background='red', bordercolor='black')
s.configure("green.Horizontal.TProgressbar", troughcolor='white', background='green', bordercolor='black')

#-----------------------------------------------------------------------------------------------------------------------
# DEFINE PROGRESS BAR VALUE

V = 'value'

def PCT_Fill():
    VIX[V] = VIX_PCT
    UST[V] = UST_PCT
    DAX[V] = DAX_PCT
    DXY[V] = DXY_PCT
    EUR[V] = EUR_PCT
    RUT[V] = RUT_PCT
    YEN[V] = YEN_PCT
    OIL[V] = OIL_PCT
    NIK[V] = NIK_PCT
    GLD[V] = GLD_PCT
    SPY[V] = SPY_PCT

#-----------------------------------------------------------------------------------------------------------------------
# LABELS

def Labels(Title, Position, Color1='red', Color2='black'):
    label = Button(root, text=Title, bg=Color1, fg=Color2)
    label.place(x=20, y=Position)
    return label

VIX_Label = Labels('VIX', 6)
UST_Label = Labels('US10', 44)
DAX_Label = Labels('DAX', 80)
DXY_Label = Labels('DXY', 118)
EUR_Label = Labels('EUR', 155)
RUT_Label = Labels('RUT', 191)
YEN_Label = Labels('YEN', 229)
OIL_Label = Labels('OIL', 265)
NIK_Label = Labels('NIK', 302, Color1='green')
GLD_Label = Labels('GLD', 339, Color1='green')
SPY_Label = Labels('SPY', 377, Color1='green')

#-----------------------------------------------------------------------------------------------------------------------
# PROGRESS BARS

O = 'horizontal'
L = 200
M = 'determinate'
Red = "red.Horizontal.TProgressbar"
Green = "green.Horizontal.TProgressbar"

VIX = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
UST = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
DAX = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
DXY = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
EUR = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
RUT = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
YEN = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
OIL = ttk.Progressbar(root, style=Red, orient=O, length=L, mode=M)
NIK = ttk.Progressbar(root, style=Green, orient=O, length=L, mode=M)
GLD = ttk.Progressbar(root, style=Green, orient=O, length=L, mode=M)
SPY = ttk.Progressbar(root, style=Green, orient=O, length=L, mode=M)

def pack(Ticker):
    Ticker.pack(pady=7)

Finalise = [VIX, UST, DAX, DXY, EUR, RUT, YEN, OIL, NIK, GLD, SPY]
for Finalise in Finalise:
    pack(Finalise)

PCT_Fill()
root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------