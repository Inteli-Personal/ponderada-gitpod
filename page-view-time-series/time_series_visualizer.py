import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True,
)
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]
def draw_line_plot():
    df_line_plt = df.copy()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_line_plt.index, df_line_plt["value"], color="r", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("Page_View_Time_Series_Visualizer/line_plot.png")
    return fig


def draw_bar_plot():
    df_bar_plt = df.copy()
    df_bar_plt["year"] = df_bar_plt.index.year
    df_bar_plt["month"] = df_bar_plt.index.month
    df_bar_plt = df_bar_plt.groupby(["year", "month"])["value"].mean().unstack()
    fig = df_bar_plt.plot(kind="bar", figsize=(12, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(
        title="Months",
        labels=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
    )
    fig.savefig("Page_View_Time_Series_Visualizer/bar_plot.png")
    return fig


def draw_box_plot():
    df_box_plt = df.copy()
    df_box_plt.reset_index(inplace=True)
    df_box_plt["year"] = [d.year for d in df_box_plt.date]
    df_box_plt["month"] = [d.strftime("%b") for d in df_box_plt.date]
    df_box_plt["month_num"] = df_box_plt["date"].dt.month
    df_box_plt = df_box_plt.sort_values("month_num")
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    sns.boxplot(x="year", y="value", data=df_box_plt, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    sns.boxplot(x="month", y="value", data=df_box_plt, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    fig.savefig("Page_View_Time_Series_Visualizer/box_plot.png")
    return fig
