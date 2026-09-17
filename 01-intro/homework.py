import marimo

__generated_with = "0.23.14"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    pd.__version__
    return


@app.cell
def _(pd):
    data = pd.read_csv("car_fuel_efficiency_2026.csv")
    return (data,)


@app.cell
def _(data):
    data.describe()
    return


@app.cell
def _(data):
    data.info(verbose=True)
    return


@app.cell
def _(data):
    data.head(n=5)
    return


@app.cell
def _(data):
    data.fuel_type.unique()
    return


@app.cell
def _(data):
    data.columns[data.isna().any(axis=0)]
    return


@app.cell
def _(data, fuel):
    data.loc[fuel]
    return


if __name__ == "__main__":
    app.run()
