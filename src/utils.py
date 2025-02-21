import matplotlib.pyplot as plt
import seaborn as sns


def plot_time_series(data, title="Brent Oil Prices"):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="Price", data=data)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.show()


def save_plot(fig, filename):
    fig.savefig(f"reports/visualizations/{filename}.png", dpi=300)
