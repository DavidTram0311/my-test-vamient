import matplotlib.pyplot as plt
import pandas as pd

def plot_signals(df):

    # Convert 'datetime' to datetime type for proper plotting
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Creating a figure and a main axes
    fig, ax1 = plt.subplots(figsize=(20, 10))

    # Plotting the smoothed mid price on the primary y-axis
    color = 'tab:blue'
    ax1.plot(df['datetime'], df['mid_px_smooth'], label='Smoothed Mid Price', color=color, linewidth=1)
    ax1.set_xlabel('Datetime')
    ax1.set_ylabel('Mid Price', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True)

    # Create a second y-axis for the smoothed buy and sell signals
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.plot(df['datetime'], df['buy_signal_smooth'], label='Smoothed Buy Signal', color='green', linewidth=1)
    ax2.plot(df['datetime'], df['sell_signal_smooth'], label='Smoothed Sell Signal', color='red', linewidth=1)
    ax2.set_ylabel('Signal Value')
    ax2.tick_params(axis='y')

    # Adding a title and a legend
    fig.suptitle('Smoothed Mid Price and Trading Signals Over Time')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

    # Show the plot
    plt.show()
