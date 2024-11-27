import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("C:/Users/Ziad/Desktop/Data Analysis Projects/boilerplate-sea-level-predictor/epa-sea-level.csv")
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15,10))
    plt.scatter(x,y)
    # plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    line1 = linregress(x,y)
    x_predict = pd.Series([i for i in range(1880,2051)])
    y_predict =  line1.slope * x_predict + line1.intercept    # y = mx +c
    plt.plot(x_predict,y_predict, 'r',lw=3)
    # plt.plot(x_predict, line1.slope * x_predict + line1.intercept, 'r',linewidth=3)
    
    # Create second line of best fit (since the year 2000).
    # subset dataframe
    df_from_2000 = df[df['Year']>= 2000]
    new_x = df_from_2000['Year']
    new_y = df_from_2000['CSIRO Adjusted Sea Level']

    line2 = linregress(new_x,new_y)
    new_x_predict = pd.Series([i for i in range(2000,2051)])
    new_y_predict =  line2.slope * new_x_predict + line2.intercept  
    plt.plot(new_x_predict, new_y_predict, 'g',lw=3)
    # plt.plot(df_from_2000['Year'],line2.slope * df_from_2000['Year']+line2.intercept, 'g',linewidth=3)


    # Add labels and title
    ax.set_xlabel('Year',fontsize=24)
    ax.set_ylabel('Sea Level (inches)',fontsize=24)
    ax.set_title('Rise in Sea Level',fontsize=30)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
