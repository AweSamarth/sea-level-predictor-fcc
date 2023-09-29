#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df =pd.read_csv('epa-sea-level.csv')
    # print(df)

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    ax= plt.gca()

    # Create first line of best fit
    regression1=linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope1= regression1.slope
    intercept1 = regression1.intercept
    # print(slope1)
    # print(intercept1)
    # print(regression1)

    x_vals1 = np.arange(df['Year'].min(), 2051)
    # print(x_vals1)
    y_vals1 = intercept1 + slope1*x_vals1
    # print(y_vals1)
    plt.plot(x_vals1, y_vals1, '-')



    # Create second line of best fit

    regression2=linregress((df['Year'][(df['Year']>=2000)]), df['CSIRO Adjusted Sea Level'][df['Year']>=2000])
    # print(regression2)
    slope2 = regression2.slope
    intercept2=regression2.intercept
    x_vals2 = np.arange(2000, 2051)

    y_vals2=intercept2 + slope2*x_vals2
    plt.plot(x_vals2, y_vals2, '--')



    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    ax.set_xticks(range(1850, 2100, 25))

    # print(plt.xlim())
    # print(plt.get_figlabels())

    # plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
