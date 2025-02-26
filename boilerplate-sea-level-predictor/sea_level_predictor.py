import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # print(df['Year'].min())
    # print(df['CSIRO Adjusted Sea Level'])
    # Create scatter plot
    fig,ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(1880, 2051)
    ax.plot(years, res.intercept + res.slope*years)

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    years2 = np.arange(2000, 2051)
    ax.plot(years2, res2.intercept + res2.slope*years2)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()