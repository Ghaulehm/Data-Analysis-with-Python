import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.core.pylabtools import figsize
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=["date"])
df.set_index('date', inplace=True)
# print(df.head())

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
        ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32,10))
    ax.plot(df.index, df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month.map(lambda x: months[x-1])
    # print(df_bar)
    df_bar = df_bar.pivot_table(index="year", columns='month', values="value", fill_value=0)
    df_bar = df_bar[months]
    # print(df_bar)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=figsize(15.14,13.3))
    categories = set(df_bar.index)
    x = np.arange(len(categories))
    bar_width = 0.06
    for i in range(12):
        ax.bar(x+(i-6)*bar_width, df_bar[months[i]], width=bar_width, label=months[i])
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=90, size=14)
    ax.set_xlabel('Years', size=16)
    ax.set_ylabel('Average Page Views', size=16)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend(title='Months', fontsize=14)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

ordered_months = [month[:3] for month in months]
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # print(ordered_months)
    df_box['month'] = pd.Categorical(df_box['month'], categories=ordered_months, ordered=True)
    df_box = df_box.sort_values('month')
    # print(df_box)
    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1,2)
    sns.boxplot(x='year',
                y='value',
                data=df_box,
                ax=axs[0])
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x='month',
                y='value',
                data=df_box,
                ax=axs[1])
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
