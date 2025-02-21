import matplotlib.pyplot as plt
import seaborn as sns


def plot_time_series(data, title="Brent Oil Prices"):
    """
    Plots the time series of Brent oil prices.

    Parameters:
        data (pd.DataFrame): DataFrame containing 'Date' and 'Price' columns.
        title (str): Title of the plot.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="Price", data=data)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.show()


def save_plot(fig, filename):
    """
    Saves a plot to the specified file.

    Parameters:
        fig (matplotlib.figure.Figure): Figure object to save.
        filename (str): Name of the file (without extension).

    Returns:
        None
    """
    fig.savefig(f"reports/visualizations/{filename}.png", dpi=300)
