"""
matplotlib.pyplot as plt
import numpy
import pandas


read_c = pandas.read_csv("C:/Users/User/Downloads/data.csv")
print(read_c)

plt.plot(read_c['Close'])
plt.show()
"""

import numpy as np
import pandas as pd
import bs4 as bs
import pickle
import requests
import os
import time
import tkinter as tk
import random
import yfinance as yf
import matplotlib.pyplot as plt

# ['ADANIENT', 'ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SUNPHARMA', 'TATAMOTORS', 'TATASTEEL', 'TCS', 'TATACONSUM', 'TECHM', 'TITAN', 'ULTRACEMCO', 'UPL', 'WIPRO']
# Extract Current top 50 Stocks which are part of Nifty50

import random


# Define the rectangle colors
colors = [('green', 'white'), ('yellow', 'black'), ('orange', 'black'), ('red', 'white')]
#colors

def colori(target):
    col="white"
    if .25 > target >= 0:
        col= "#91FFAE"
    elif .5 > target >= .25:
        col= "#55FD80"
    elif .75 > target >= .5:
        col= "#20FD59"
    elif 1 > target >= .75:
        col= "#01ED3E"
    elif 1.5 > target >= 1:
        col= "#01C233"
    elif 2.5 > target >= 1.5:
        col= "#23AA0B"
    elif 20 > target >= 2.5:
        col= "#207012"
    elif -.25 < target < 0:
        col= "#FEBEBE"
    elif -.5 < target <= -.25:
        col= "#FC8686"
    elif -.75 < target <= -.5:
        col= "#FE5D5D"
    elif -1 < target <= -.75:
        col= "#FC2626"
    elif -1.5 < target <= -1:
        col= "#FF0000"
    elif -2.5 < target <= -1.5:
        col= "#D00000"
    elif -20 < target <= -2.5:
        col= "#A40202"
    return col

def save_nifty50_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'id': 'constituents'})
    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker)
    with open('NIFTY_50.pickle', 'wb') as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

# Tickers:- Conatains all the symbols of the stocks
dff = pd.DataFrame([], columns=['ticker','change'])
i = 0
# Get 1 min data for each symbol within a period of 7days
def get_data_from_yahoo(reload_nifty50=False):
    if reload_nifty50:
        tickers = save_nifty50_tickers()
    else:
        with open('NIFTY_50.pickle', 'rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    # start = dt.datetime(2010,1,1)
    # end = dt.datetime.now()
    for ticker in tickers:
        print(ticker)
        # if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):

        stock_data = yf.download(ticker+".NS", period='3d')
        # Calculate the percentage change in the stock's price today
        print(stock_data)
        last_close = stock_data['Close'].iloc[-2]  # Last closing price
        current_price = stock_data['Close'].iloc[-1]  # Current price
        percent_change = (current_price - last_close) / last_close * 100
        global i
        k = [ticker, round(percent_change, 2)]
        dff.loc[i] = k
        i = i+1
        if i==50:
            i=0
        else:
            continue

        # Print the percentage change
        print(ticker, 'Today\'s percentage change:', round(percent_change, 2), '%')

    # else:
    # 	print('Already have {}'.format(ticker))
#get_data_from_yahoo(True)
print(dff)

# Create the main window
root = tk.Tk()

# Get the resolution of the full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height, screen_width)
# Set the window size and position to fill the screen
root.geometry('{}x{}+0+0'.format(screen_width, screen_height))

# Create a canvas to fill the window
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

# Define the rectangle coordinates and text coordinates
rect38_coords = ((1366-201-116)*screen_width/1366, (768-244-116-100)*screen_height/768, (1366-201)*screen_width/1366, (768-244-116)*screen_height/768) #jswsteel
rect1_coords = (screen_width/1366, 1*screen_height/768, 322*screen_width/1366, 322*screen_height/768) #reliance
rect2_coords = (322*screen_width/1366, 1*screen_height/768, (322+191)*screen_width/1366, 191*screen_height/768) #HindustanUniliver
rect3_coords = ((322+191)*screen_width/1366, 1*screen_height/768, (322+191+183)*screen_width/1366, 183*screen_height/768) #itc
rect4_coords = ((322+191+183)*screen_width/1366, 1*screen_height/768, (322+191+183+118)*screen_width/1366, 118*screen_height/768) #adanient
rect5_coords = (814*screen_width/1366, 1*screen_height/768, (814+96)*screen_width/1366, 96*screen_height/768) #adaniports
rect6_coords = ((1366-128-101)*screen_width/1366, 101*screen_height/768, (1366-128)*screen_width/1366, (101+78.4)*screen_height/768) #bajajauto
rect7_coords = ((1366-229-91-136)*screen_width/1366, 1*screen_height/768, (1366-229-91)*screen_width/1366, 154.6*screen_height/768) #l&t
rect8_coords = ((1366-229-91)*screen_width/1366, 1*screen_height/768, (1366-229)*screen_width/1366, 91*screen_height/768) #tatasteel
rect9_coords = ((1366-98)*screen_width/1366, 128*screen_height/768, 1366*screen_width/1366, (128+98)*screen_height/768) #m&m
rect10_coords = ((1366-128-101)*screen_width/1366, 1*screen_height/768, (1366-128)*screen_width/1366, 101*screen_height/768) #tatamotors
rect11_coords = ((1366-128)*screen_width/1366, 1*screen_height/768, 1366*screen_width/1366, 128*screen_height/768) #maruti
rect12_coords = ((1366-98-120.7)*screen_width/1366, 179.4*screen_height/768, (1366-98)*screen_width/1366, (179.4+46.6)*screen_height/768) #eichermotors
rect13_coords = ((322)*screen_width/1366, (191)*screen_height/768, (322+101)*screen_width/1366, (191+131)*screen_height/768) #nestleindia
rect14_coords = ((322+101)*screen_width/1366, (191)*screen_height/768, (322+101+111.7)*screen_width/1366, (191+131)*screen_height/768) #titan
rect15_coords = ((322+191+183)*screen_width/1366, (118)*screen_height/768, (322+191+183+118)*screen_width/1366, (118+58)*screen_height/768) #britania
rect16_coords = ((1366-128-101-39)*screen_width/1366, 144*screen_height/768, (1366-128-101)*screen_width/1366, 226*screen_height/768) #heromotocorp
rect17_coords = (((1366-229-91))*screen_width/1366, 91*screen_height/768, (1366-229)*screen_width/1366, (91+54)*screen_height/768) #bpcl
rect18_coords = ((1366-128-101-39-84)*screen_width/1366, 154.6*screen_height/768, (1366-128-101-39)*screen_width/1366, (154.6+82-9.4)*screen_height/768) #hinadalco
rect19_coords = ((322+101+111.7+107-54)*screen_width/1366, 183*screen_height/768, (322+191+183+54)*screen_width/1366, (131+17+191)*screen_height/768) #powergrid
rect20_coords = ((1366-229-91-136)*screen_width/1366, 154.6*screen_height/768, (1366-128-101-39-84)*screen_width/1366, (154.6+131.6)*screen_height/768) #ultracemenco
rect21_coords = ((1366-229-91-136)*screen_width/1366, (154.6+131.6)*screen_height/768, (1366-229-91-136+113)*screen_width/1366, (768-180-64-145)*screen_height/768) #ntpc
rect22_coords = ((322+191+183+118)*screen_width/1366, (96+94)*screen_height/768, (1366-229-91-136)*screen_width/1366, (96+94+130.6)*screen_height/768) #ongc
rect23_coords = ((322+191+183)*screen_width/1366, (118+58)*screen_height/768, (322+191+183+118)*screen_width/1366, (118+58+147.6)*screen_height/768) #asianpaints
rect24_coords = ((115+135)*screen_width/1366, (191+131+74+64.6)*screen_height/768, (115+135+89.46)*screen_width/1366, (768-183-84.6)*screen_height/768) #upl
rect25_coords = (273*screen_width/1366, (768-183-84.6)*screen_height/768, (273+84.6)*screen_width/1366, (768-183)*screen_height/768) #grasim
rect26_coords = ((115+135+64)*screen_width/1366, (191+131+74)*screen_height/768, (115+135+64+78)*screen_width/1366, (191+131+74+64.6)*screen_height/768) #drreddy
rect27_coords = ((115+135+68)*screen_width/1366, (191+131)*screen_height/768, (115+135+68+74)*screen_width/1366, (191+131+74)*screen_height/768) #divisilab
rect28_coords = ((115+135)*screen_width/1366, (191+131+68)*screen_height/768, (115+135+64)*screen_width/1366, (191+131+64+68)*screen_height/768) #apollohospitl
rect29_coords = ((250-164)*screen_width/1366, 322*screen_height/768, 250*screen_width/1366, (322+38)*screen_height/768) #techmahindra
rect30_coords = (1*screen_width/1366, 322*screen_height/768, 81*screen_width/1366, (322+57)*screen_height/768) #tataConsumer
rect31_coords = ((115)*screen_width/1366, (768-273-135)*screen_height/768, (115+135)*screen_width/1366, (768-273)*screen_height/768) #hcltech
rect32_coords = (1*screen_width/1366, (768-273-115)*screen_height/768, 115*screen_width/1366, (768-273)*screen_height/768) #wipro
rect33_coords = (1*screen_width/1366, (768-273)*screen_height/768, 273*screen_width/1366, 768*screen_height/768) #tcs
rect34_coords = ((273)*screen_width/1366, (768-183)*screen_height/768, (273+183)*screen_width/1366, 768*screen_height/768) #infy
rect35_coords = ((273+183)*screen_width/1366, (768-168)*screen_height/768, (273+183+178)*screen_width/1366, 768*screen_height/768) #bhartiairtel
rect36_coords = ((115+135)*screen_width/1366, (191+131)*screen_height/768, (115+135+68)*screen_width/1366, (191+131+68)*screen_height/768) #cipla
rect37_coords = ((322+101+111.7)*screen_width/1366, 183*screen_height/768, (322+101+111.7+107)*screen_width/1366, (191+131)*screen_height/768) #sunpharma

rect39_coords = ((322+191+183+118)*screen_width/1366, 96*screen_height/768, (1366-229-91-136)*screen_width/1366, (96+94)*screen_height/768) #coalindia
rect40_coords = ((1366-201-116-168)*screen_width/1366, (768-180-64-145)*screen_height/768, (1366-201-116)*screen_width/1366, (768-180-64)*screen_height/768) #kotakbank
rect41_coords = ((1366-201-116)*screen_width/1366, (768-244-116)*screen_height/768, (1366-201)*screen_width/1366, (768-244)*screen_height/768) #bajajfinsv
rect42_coords = ((1366-244-120.7-120.3)*screen_width/1366, (768-180-64)*screen_height/768, (1366-244-120.7)*screen_width/1366, (768-180)*screen_height/768) #hdfclife
rect43_coords = ((1366-244-120.7)*screen_width/1366, (768-180-64)*screen_height/768, (1366-244)*screen_width/1366, (768-180)*screen_height/768) #sbilife
rect44_coords = ((1366-247.6)*screen_width/1366, 226*screen_height/768, 1366*screen_width/1366, (226+97)*screen_height/768) #bajajfinance
rect45_coords = ((1366-244-180-110.3)*screen_width/1366, (768-129-51)*screen_height/768, ((1366-244-180))*screen_width/1366, (768-129)*screen_height/768) #indusindbank
rect46_coords = ((1366-201)*screen_width/1366, (768-244-201)*screen_height/768, 1366*screen_width/1366, (768-244)*screen_height/768) #icicicbank
rect47_coords = ((1366-244-180-129-179)*screen_width/1366, (768-179)*screen_height/768, (1366-244-180-129)*screen_width/1366, 768*screen_height/768) #hdfc
rect48_coords = ((1366-244-180-129)*screen_width/1366, (768-129)*screen_height/768, (1366-244-180)*screen_width/1366, 768*screen_height/768) #axis
rect49_coords = ((1366-244-180)*screen_width/1366, (768-180)*screen_height/768, (1366-244)*screen_width/1366, 768*screen_height/768) #sbin
rect50_coords = ((1366-244)*screen_width/1366, (768-244)*screen_height/768, 1366*screen_width/1366, 768*screen_height/768) #hdfcbank




rect1_text_coords = ((rect1_coords[0] + rect1_coords[2]) / 2, (rect1_coords[1] + rect1_coords[3]) / 2)
rect2_text_coords = ((rect2_coords[0] + rect2_coords[2]) / 2, (rect2_coords[1] + rect2_coords[3]) / 2)
rect3_text_coords = ((rect3_coords[0] + rect3_coords[2]) / 2, (rect3_coords[1] + rect3_coords[3]) / 2)
rect4_text_coords = ((rect4_coords[0] + rect4_coords[2]) / 2, (rect4_coords[1] + rect4_coords[3]) / 2)
rect5_text_coords = ((rect5_coords[0] + rect5_coords[2]) / 2, (rect5_coords[1] + rect5_coords[3]) / 2)
rect6_text_coords = ((rect6_coords[0] + rect6_coords[2]) / 2, (rect6_coords[1] + rect6_coords[3]) / 2)
rect7_text_coords = ((rect7_coords[0] + rect7_coords[2]) / 2, (rect7_coords[1] + rect7_coords[3]) / 2)
rect8_text_coords = ((rect8_coords[0] + rect8_coords[2]) / 2, (rect8_coords[1] + rect8_coords[3]) / 2)
rect9_text_coords = ((rect9_coords[0] + rect9_coords[2]) / 2, (rect9_coords[1] + rect9_coords[3]) / 2)
rect10_text_coords = ((rect10_coords[0] + rect10_coords[2]) / 2, (rect10_coords[1] + rect10_coords[3]) / 2)
rect11_text_coords = ((rect11_coords[0] + rect11_coords[2]) / 2, (rect11_coords[1] + rect11_coords[3]) / 2)
rect12_text_coords = ((rect12_coords[0] + rect12_coords[2]) / 2, (rect12_coords[1] + rect12_coords[3]) / 2)
rect13_text_coords = ((rect13_coords[0] + rect13_coords[2]) / 2, (rect13_coords[1] + rect13_coords[3]) / 2)
rect14_text_coords = ((rect14_coords[0] + rect14_coords[2]) / 2, (rect14_coords[1] + rect14_coords[3]) / 2)
rect15_text_coords = ((rect15_coords[0] + rect15_coords[2]) / 2, (rect15_coords[1] + rect15_coords[3]) / 2)
rect16_text_coords = ((rect16_coords[0] + rect16_coords[2]) / 2, (rect16_coords[1] + rect16_coords[3]) / 2)
rect17_text_coords = ((rect17_coords[0] + rect17_coords[2]) / 2, (rect17_coords[1] + rect17_coords[3]) / 2)
rect18_text_coords = ((rect18_coords[0] + rect18_coords[2]) / 2, (rect18_coords[1] + rect18_coords[3]) / 2)
rect19_text_coords = ((rect19_coords[0] + rect19_coords[2]) / 2, (rect19_coords[1] + rect19_coords[3]) / 2)
rect20_text_coords = ((rect20_coords[0] + rect20_coords[2]) / 2, (rect20_coords[1] + rect20_coords[3]) / 2)
rect21_text_coords = ((rect21_coords[0] + rect21_coords[2]) / 2, (rect21_coords[1] + rect21_coords[3]) / 2)
rect22_text_coords = ((rect22_coords[0] + rect22_coords[2]) / 2, (rect22_coords[1] + rect22_coords[3]) / 2)
rect23_text_coords = ((rect23_coords[0] + rect23_coords[2]) / 2, (rect23_coords[1] + rect23_coords[3]) / 2)
rect24_text_coords = ((rect24_coords[0] + rect24_coords[2]) / 2, (rect24_coords[1] + rect24_coords[3]) / 2)
rect25_text_coords = ((rect25_coords[0] + rect25_coords[2]) / 2, (rect25_coords[1] + rect25_coords[3]) / 2)
rect26_text_coords = ((rect26_coords[0] + rect26_coords[2]) / 2, (rect26_coords[1] + rect26_coords[3]) / 2)
rect27_text_coords = ((rect27_coords[0] + rect27_coords[2]) / 2, (rect27_coords[1] + rect27_coords[3]) / 2)
rect28_text_coords = ((rect28_coords[0] + rect28_coords[2]) / 2, (rect28_coords[1] + rect28_coords[3]) / 2)
rect29_text_coords = ((rect29_coords[0] + rect29_coords[2]) / 2, (rect29_coords[1] + rect29_coords[3]) / 2)
rect30_text_coords = ((rect30_coords[0] + rect30_coords[2]) / 2, (rect30_coords[1] + rect30_coords[3]) / 2)
rect31_text_coords = ((rect31_coords[0] + rect31_coords[2]) / 2, (rect31_coords[1] + rect31_coords[3]) / 2)
rect32_text_coords = ((rect32_coords[0] + rect32_coords[2]) / 2, (rect32_coords[1] + rect32_coords[3]) / 2)
rect33_text_coords = ((rect33_coords[0] + rect33_coords[2]) / 2, (rect33_coords[1] + rect33_coords[3]) / 2)
rect34_text_coords = ((rect34_coords[0] + rect34_coords[2]) / 2, (rect34_coords[1] + rect34_coords[3]) / 2)
rect35_text_coords = ((rect35_coords[0] + rect35_coords[2]) / 2, (rect35_coords[1] + rect35_coords[3]) / 2)
rect36_text_coords = ((rect36_coords[0] + rect36_coords[2]) / 2, (rect36_coords[1] + rect36_coords[3]) / 2)
rect37_text_coords = ((rect37_coords[0] + rect37_coords[2]) / 2, (rect37_coords[1] + rect37_coords[3]) / 2)
rect38_text_coords = ((rect38_coords[0] + rect38_coords[2]) / 2, (rect38_coords[1] + rect38_coords[3]) / 2)
rect39_text_coords = ((rect39_coords[0] + rect39_coords[2]) / 2, (rect39_coords[1] + rect39_coords[3]) / 2)
rect40_text_coords = ((rect40_coords[0] + rect40_coords[2]) / 2, (rect40_coords[1] + rect40_coords[3]) / 2)
rect41_text_coords = ((rect41_coords[0] + rect41_coords[2]) / 2, (rect41_coords[1] + rect41_coords[3]) / 2)
rect42_text_coords = ((rect42_coords[0] + rect42_coords[2]) / 2, (rect42_coords[1] + rect42_coords[3]) / 2)
rect43_text_coords = ((rect43_coords[0] + rect43_coords[2]) / 2, (rect43_coords[1] + rect43_coords[3]) / 2)
rect44_text_coords = ((rect44_coords[0] + rect44_coords[2]) / 2, (rect44_coords[1] + rect44_coords[3]) / 2)
rect45_text_coords = ((rect45_coords[0] + rect45_coords[2]) / 2, (rect45_coords[1] + rect45_coords[3]) / 2)
rect46_text_coords = ((rect46_coords[0] + rect46_coords[2]) / 2, (rect46_coords[1] + rect46_coords[3]) / 2)
rect47_text_coords = ((rect47_coords[0] + rect47_coords[2]) / 2, (rect47_coords[1] + rect47_coords[3]) / 2)
rect48_text_coords = ((rect48_coords[0] + rect48_coords[2]) / 2, 960*(rect48_coords[1] + rect48_coords[3]) / 2000)
rect49_text_coords = ((rect49_coords[0] + rect49_coords[2]) / 2, (rect49_coords[1] + rect49_coords[3]) / 2)
rect50_text_coords = ((rect50_coords[0] + rect50_coords[2]) / 2, (rect50_coords[1] + rect50_coords[3]) / 2)


# Draw the rectangles and text
rect1 = canvas.create_rectangle(*rect1_coords, fill=colors[0][0], outline='black')
rect2 = canvas.create_rectangle(*rect2_coords, fill=colors[0][0], outline='black')
rect3 = canvas.create_rectangle(*rect3_coords, fill=colors[0][0], outline='black')
rect4 = canvas.create_rectangle(*rect4_coords, fill=colors[0][0], outline='black')
rect5 = canvas.create_rectangle(*rect5_coords, fill=colors[0][0], outline='black')
rect6 = canvas.create_rectangle(*rect6_coords, fill=colors[0][0], outline='black')
rect7 = canvas.create_rectangle(*rect7_coords, fill=colors[0][0], outline='black')
rect8 = canvas.create_rectangle(*rect8_coords, fill=colors[0][0], outline='black')
rect9 = canvas.create_rectangle(*rect9_coords, fill=colors[0][0], outline='black')
rect10 = canvas.create_rectangle(*rect10_coords, fill=colors[0][0], outline='black')
rect11 = canvas.create_rectangle(*rect11_coords, fill=colors[0][0], outline='black')
rect12 = canvas.create_rectangle(*rect12_coords, fill=colors[0][0], outline='black')
rect13 = canvas.create_rectangle(*rect13_coords, fill=colors[0][0], outline='black')
rect14 = canvas.create_rectangle(*rect14_coords, fill=colors[0][0], outline='black')
rect15 = canvas.create_rectangle(*rect15_coords, fill=colors[0][0], outline='black')
rect16 = canvas.create_rectangle(*rect16_coords, fill=colors[0][0], outline='black')
rect17 = canvas.create_rectangle(*rect17_coords, fill=colors[0][0], outline='black')
rect18 = canvas.create_rectangle(*rect18_coords, fill=colors[0][0], outline='black')
rect19 = canvas.create_rectangle(*rect19_coords, fill=colors[0][0], outline='black')
rect20 = canvas.create_rectangle(*rect20_coords, fill=colors[0][0], outline='black')
rect21 = canvas.create_rectangle(*rect21_coords, fill=colors[0][0], outline='black')
rect22 = canvas.create_rectangle(*rect22_coords, fill=colors[0][0], outline='black')
rect23 = canvas.create_rectangle(*rect23_coords, fill=colors[0][0], outline='black')
rect24 = canvas.create_rectangle(*rect24_coords, fill=colors[0][0], outline='black')
rect25 = canvas.create_rectangle(*rect25_coords, fill=colors[0][0], outline='black')
rect26 = canvas.create_rectangle(*rect26_coords, fill=colors[0][0], outline='black')
rect27 = canvas.create_rectangle(*rect27_coords, fill=colors[0][0], outline='black')
rect28 = canvas.create_rectangle(*rect28_coords, fill=colors[0][0], outline='black')
rect29 = canvas.create_rectangle(*rect29_coords, fill=colors[0][0], outline='black')
rect30 = canvas.create_rectangle(*rect30_coords, fill=colors[0][0], outline='black')
rect31 = canvas.create_rectangle(*rect31_coords, fill=colors[0][0], outline='black')
rect32 = canvas.create_rectangle(*rect32_coords, fill=colors[0][0], outline='black')
rect33 = canvas.create_rectangle(*rect33_coords, fill=colors[0][0], outline='black')
rect34 = canvas.create_rectangle(*rect34_coords, fill=colors[0][0], outline='black')
rect35 = canvas.create_rectangle(*rect35_coords, fill=colors[0][0], outline='black')
rect36 = canvas.create_rectangle(*rect36_coords, fill=colors[0][0], outline='black')
rect37 = canvas.create_rectangle(*rect37_coords, fill=colors[0][0], outline='black')
rect38 = canvas.create_rectangle(*rect38_coords, fill=colors[0][0], outline='black')
rect39 = canvas.create_rectangle(*rect39_coords, fill=colors[0][0], outline='black')
rect40 = canvas.create_rectangle(*rect40_coords, fill=colors[0][0], outline='black')
rect41 = canvas.create_rectangle(*rect41_coords, fill=colors[0][0], outline='black')
rect42 = canvas.create_rectangle(*rect42_coords, fill=colors[0][0], outline='black')
rect43 = canvas.create_rectangle(*rect43_coords, fill=colors[0][0], outline='black')
rect44 = canvas.create_rectangle(*rect44_coords, fill=colors[0][0], outline='black')
rect45 = canvas.create_rectangle(*rect45_coords, fill=colors[0][0], outline='black')
rect46 = canvas.create_rectangle(*rect46_coords, fill=colors[0][0], outline='black')
rect47 = canvas.create_rectangle(*rect47_coords, fill=colors[0][0], outline='black')
rect48 = canvas.create_rectangle(*rect48_coords, fill=colors[0][0], outline='black')
rect49 = canvas.create_rectangle(*rect49_coords, fill=colors[0][0], outline='black')
rect50 = canvas.create_rectangle(*rect50_coords, fill=colors[0][0], outline='black')


rect1_text = canvas.create_text(*rect1_text_coords, text=colors[0][1], fill=colors[0][0], font=('bold', 15))
rect2_text = canvas.create_text(*rect2_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect3_text = canvas.create_text(*rect3_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect4_text = canvas.create_text(*rect4_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect5_text = canvas.create_text(*rect5_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect6_text = canvas.create_text(*rect6_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect7_text = canvas.create_text(*rect7_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect8_text = canvas.create_text(*rect8_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect9_text = canvas.create_text(*rect9_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect10_text = canvas.create_text(*rect10_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect11_text = canvas.create_text(*rect11_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect12_text = canvas.create_text(*rect12_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect13_text = canvas.create_text(*rect13_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 10))
rect14_text = canvas.create_text(*rect14_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect15_text = canvas.create_text(*rect15_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect16_text = canvas.create_text(*rect16_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect17_text = canvas.create_text(*rect17_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect18_text = canvas.create_text(*rect18_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect19_text = canvas.create_text(*rect19_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 7))
rect20_text = canvas.create_text(*rect20_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect21_text = canvas.create_text(*rect21_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect22_text = canvas.create_text(*rect22_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect23_text = canvas.create_text(*rect23_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect24_text = canvas.create_text(*rect24_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect25_text = canvas.create_text(*rect25_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect26_text = canvas.create_text(*rect26_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect27_text = canvas.create_text(*rect27_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect28_text = canvas.create_text(*rect28_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect29_text = canvas.create_text(*rect29_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect30_text = canvas.create_text(*rect30_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect31_text = canvas.create_text(*rect31_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect32_text = canvas.create_text(*rect32_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect33_text = canvas.create_text(*rect33_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect34_text = canvas.create_text(*rect34_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect35_text = canvas.create_text(*rect35_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect36_text = canvas.create_text(*rect36_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect37_text = canvas.create_text(*rect37_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect38_text = canvas.create_text(*rect38_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect39_text = canvas.create_text(*rect39_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect40_text = canvas.create_text(*rect40_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect41_text = canvas.create_text(*rect41_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect42_text = canvas.create_text(*rect42_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect43_text = canvas.create_text(*rect43_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect44_text = canvas.create_text(*rect44_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect45_text = canvas.create_text(*rect45_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect46_text = canvas.create_text(*rect46_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect47_text = canvas.create_text(*rect47_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect48_text = canvas.create_text(*rect48_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect49_text = canvas.create_text(*rect49_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))
rect50_text = canvas.create_text(*rect50_text_coords, text=colors[0][1], fill=colors[0][0], font=('Arial', 12))


# Loop to update the rectangle colors and text
def update_colors():
    print("11111111111111111")
    get_data_from_yahoo(True)
    print("2222222222222222222222222222")
    print(dff)
    # Read the market data (replace with your own code to read live market data)
    market_data = random.randint(0, 100)
    # Update the rectangle colors and text based on the market data
    color_index = min(int(market_data / 25), 3)
    color = colors[color_index][0]
    text_color = colors[color_index][1]
    canvas.itemconfig(rect1, fill=colori(dff['change'][37]))
    canvas.itemconfig(rect2, fill=colori(dff['change'][23]))
    canvas.itemconfig(rect3, fill=colori(dff['change'][27]))
    canvas.itemconfig(rect4, fill=colori(dff['change'][0]))
    canvas.itemconfig(rect5, fill=colori(dff['change'][1]))
    canvas.itemconfig(rect6, fill=colori(dff['change'][5]))
    canvas.itemconfig(rect7, fill=colori(dff['change'][30]))
    canvas.itemconfig(rect8, fill=colori(dff['change'][42]))
    canvas.itemconfig(rect9, fill=colori(dff['change'][31]))
    canvas.itemconfig(rect10, fill=colori(dff['change'][41]))
    canvas.itemconfig(rect11, fill=colori(dff['change'][32]))
    canvas.itemconfig(rect12, fill=colori(dff['change'][15]))
    canvas.itemconfig(rect13, fill=colori(dff['change'][33]))
    canvas.itemconfig(rect14, fill=colori(dff['change'][46]))
    canvas.itemconfig(rect15, fill=colori(dff['change'][10]))
    canvas.itemconfig(rect16, fill=colori(dff['change'][21]))
    canvas.itemconfig(rect17, fill=colori(dff['change'][8]))
    canvas.itemconfig(rect18, fill=colori(dff['change'][22]))
    canvas.itemconfig(rect19, fill=colori(dff['change'][36]))
    canvas.itemconfig(rect20, fill=colori(dff['change'][47]))
    canvas.itemconfig(rect21, fill=colori(dff['change'][34]))
    canvas.itemconfig(rect22, fill=colori(dff['change'][35]))
    canvas.itemconfig(rect23, fill=colori(dff['change'][3]))
    canvas.itemconfig(rect24, fill=colori(dff['change'][48]))
    canvas.itemconfig(rect25, fill=colori(dff['change'][16]))
    canvas.itemconfig(rect26, fill=colori(dff['change'][14]))
    canvas.itemconfig(rect27, fill=colori(dff['change'][13]))
    canvas.itemconfig(rect28, fill=colori(dff['change'][2]))
    canvas.itemconfig(rect29, fill=colori(dff['change'][45]))
    canvas.itemconfig(rect30, fill=colori(dff['change'][44]))
    canvas.itemconfig(rect31, fill=colori(dff['change'][17]))
    canvas.itemconfig(rect32, fill=colori(dff['change'][49]))
    canvas.itemconfig(rect33, fill=colori(dff['change'][43]))
    canvas.itemconfig(rect34, fill=colori(dff['change'][26]))
    canvas.itemconfig(rect35, fill=colori(dff['change'][9]))
    canvas.itemconfig(rect36, fill=colori(dff['change'][11]))
    canvas.itemconfig(rect37, fill=colori(dff['change'][40]))
    canvas.itemconfig(rect38, fill=colori(dff['change'][28]))
    canvas.itemconfig(rect39, fill=colori(dff['change'][12]))
    canvas.itemconfig(rect40, fill=colori(dff['change'][29]))
    canvas.itemconfig(rect41, fill=colori(dff['change'][7]))
    canvas.itemconfig(rect42, fill=colori(dff['change'][20]))
    canvas.itemconfig(rect43, fill=colori(dff['change'][38]))
    canvas.itemconfig(rect44, fill=colori(dff['change'][6]))
    canvas.itemconfig(rect45, fill=colori(dff['change'][25]))
    canvas.itemconfig(rect46, fill=colori(dff['change'][24]))
    canvas.itemconfig(rect47, fill=colori(dff['change'][18]))
    canvas.itemconfig(rect48, fill=colori(dff['change'][4]))
    canvas.itemconfig(rect49, fill=colori(dff['change'][39]))
    canvas.itemconfig(rect50, fill=colori(dff['change'][19]))

    print(len(dff),"jeeeeeeeeeeeeeeeeeeeeeei3eneeeeeeeeeeeeeeeeeeeeeeee399999999999999")
    canvas.itemconfig(rect1_text, text=(dff['ticker'][37],dff['change'][37]), fill='black')
    canvas.itemconfig(rect2_text, text=(dff['ticker'][23],dff['change'][23]), fill='black')
    canvas.itemconfig(rect3_text, text=(dff['ticker'][27],dff['change'][27]), fill='black')
    canvas.itemconfig(rect4_text, text=(dff['ticker'][0],dff['change'][0]), fill='black')
    canvas.itemconfig(rect5_text, text=(dff['ticker'][1], dff['change'][1]), fill='black')
    canvas.itemconfig(rect6_text, text=(dff['ticker'][5], dff['change'][5]), fill='black')
    canvas.itemconfig(rect7_text, text=(dff['ticker'][30], dff['change'][30]), fill='black')
    canvas.itemconfig(rect8_text, text=(dff['ticker'][42], dff['change'][42]), fill='black')
    canvas.itemconfig(rect9_text, text=(dff['ticker'][31], dff['change'][31]), fill='black')
    canvas.itemconfig(rect10_text, text=(dff['ticker'][41], dff['change'][41]), fill='black')
    canvas.itemconfig(rect11_text, text=(dff['ticker'][32], dff['change'][32]), fill='black')
    canvas.itemconfig(rect12_text, text=(dff['ticker'][15], dff['change'][15]), fill='black')
    canvas.itemconfig(rect13_text, text=(dff['ticker'][33], dff['change'][33]), fill='black')
    canvas.itemconfig(rect14_text, text=(dff['ticker'][46], dff['change'][46]), fill='black')
    canvas.itemconfig(rect15_text, text=(dff['ticker'][10], dff['change'][10]), fill='black')
    canvas.itemconfig(rect16_text, text=(dff['ticker'][21], dff['change'][21]), fill='black')
    canvas.itemconfig(rect17_text, text=(dff['ticker'][8], dff['change'][8]), fill='black')
    canvas.itemconfig(rect18_text, text=(dff['ticker'][22], dff['change'][22]), fill='black')
    canvas.itemconfig(rect19_text, text=(dff['ticker'][36], dff['change'][36]), fill='black')
    canvas.itemconfig(rect20_text, text=(dff['ticker'][47], dff['change'][47]), fill='black')
    canvas.itemconfig(rect21_text, text=(dff['ticker'][34], dff['change'][34]), fill='black')
    canvas.itemconfig(rect22_text, text=(dff['ticker'][35], dff['change'][35]), fill='black')
    canvas.itemconfig(rect23_text, text=(dff['ticker'][3], dff['change'][3]), fill='black')
    canvas.itemconfig(rect24_text, text=(dff['ticker'][48], dff['change'][48]), fill='black')
    canvas.itemconfig(rect25_text, text=(dff['ticker'][16], dff['change'][16]), fill='black')
    canvas.itemconfig(rect26_text, text=(dff['ticker'][14], dff['change'][14]), fill='black')
    canvas.itemconfig(rect27_text, text=(dff['ticker'][13], dff['change'][13]), fill='black')
    canvas.itemconfig(rect28_text, text=(dff['ticker'][2], dff['change'][2]), fill='black')
    canvas.itemconfig(rect29_text, text=(dff['ticker'][45], dff['change'][45]), fill='black')
    canvas.itemconfig(rect30_text, text=(dff['ticker'][44], dff['change'][44]), fill='black')
    canvas.itemconfig(rect31_text, text=(dff['ticker'][17], dff['change'][17]), fill='black')
    canvas.itemconfig(rect32_text, text=(dff['ticker'][49], dff['change'][49]), fill='black')
    canvas.itemconfig(rect33_text, text=(dff['ticker'][43], dff['change'][43]), fill='black')
    canvas.itemconfig(rect34_text, text=(dff['ticker'][26], dff['change'][26]), fill='black')
    canvas.itemconfig(rect35_text, text=(dff['ticker'][9], dff['change'][9]), fill='black')
    canvas.itemconfig(rect36_text, text=(dff['ticker'][11], dff['change'][11]), fill='black')
    canvas.itemconfig(rect37_text, text=(dff['ticker'][40], dff['change'][40]), fill='black')
    canvas.itemconfig(rect38_text, text=(dff['ticker'][28], dff['change'][28]), fill='black')
    canvas.itemconfig(rect39_text, text=(dff['ticker'][12], dff['change'][12]), fill='black')
    canvas.itemconfig(rect40_text, text=(dff['ticker'][29], dff['change'][29]), fill='black')
    canvas.itemconfig(rect41_text, text=(dff['ticker'][7], dff['change'][7]), fill='black')
    canvas.itemconfig(rect42_text, text=(dff['ticker'][20], dff['change'][20]), fill='black')
    canvas.itemconfig(rect43_text, text=(dff['ticker'][38], dff['change'][38]), fill='black')
    canvas.itemconfig(rect44_text, text=(dff['ticker'][6], dff['change'][6]), fill='black')
    canvas.itemconfig(rect45_text, text=(dff['ticker'][25], dff['change'][25]), fill='black')
    canvas.itemconfig(rect46_text, text=(dff['ticker'][24], dff['change'][24]), fill='black')
    canvas.itemconfig(rect47_text, text=(dff['ticker'][18], dff['change'][18]), fill='black')
    canvas.itemconfig(rect48_text, text=(dff['ticker'][4], dff['change'][4]), fill='black')
    canvas.itemconfig(rect49_text, text=(dff['ticker'][39], dff['change'][39]), fill='black')
    canvas.itemconfig(rect50_text, text=(dff['ticker'][19], dff['change'][19]), fill='black')

    #dff.drop(index=dff.index, inplace=True)
    # Call this function again after 100 milliseconds
    root.after(ms=60000, func=update_colors)


# Start the loop to update the rectangle colors and text
update_colors()

# Start the main event loop
root.mainloop()