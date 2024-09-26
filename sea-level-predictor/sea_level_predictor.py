import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Original data"
    )
    slope, intercept, _, _, _ = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    years = pd.Series(range(1880, 2051))
    sea_level = intercept + slope * years
    plt.plot(
        years,
        sea_level,
        label="Best fit line (all data)",
        color="red",
    )
    df_recent = df[df["Year"] >= 2000]
    slope, intercept, _, _, _ = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    recent_years = pd.Series(range(2000, 2051))
    sea_level = intercept + slope * recent_years
    plt.plot(
        recent_years,
        sea_level,
        label="Best fit line (from 2000)",
        color="green",
    )
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.savefig("sea_level_plot.png")
    return plt.gca()
