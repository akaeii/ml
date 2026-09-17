import marimo

__generated_with = "0.23.14"
app = marimo.App(width="full")

with app.setup:
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## **Creating Arrays**
    """)
    return


@app.cell
def _():
    np.zeros(10)
    return


@app.cell
def _():
    x = np.zeros((3,10))
    print(x.shape)
    return (x,)


@app.cell
def _(x):
    y = x.T
    print(y.shape)
    return


@app.cell
def _():
    np.zeros(5)
    return


@app.cell
def _():
    np.ones(10)
    return


@app.cell
def _():
    np.full(10, 2.5)
    return


@app.cell
def _():
    l = [1, 2, 3, 4, 5]
    np.array(l)
    return (l,)


@app.cell
def _(l):
    l[0]
    return


@app.cell
def _(l):
    l[-1]
    return


@app.cell
def _():
    np.arange(5, step=0.5)
    return


@app.cell
def _():
    np.linspace(0, 100, 12)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## **Multi-Dimentional Arrays**
    """)
    return


@app.cell
def _():
    np.full((5, 2), 3)
    return


@app.cell(hide_code=True)
def _():
    mo.ui.matrix(np.full((5, 2), 3), disabled=True)
    return


@app.cell
def _():
    md = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    md
    return (md,)


@app.cell
def _(md):
    md[2,1]
    return


@app.cell
def _(md):
    md[2,1] = 67
    md
    return


@app.cell
def _(md):
    md[1] = [67, 67,67]
    md
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## **Randomly Generated Arrays**
    """)
    return


@app.cell
def _():
    np.random.seed(2)
    np.random.rand(5,3)
    return


@app.cell
def _():
    np.random.randint(2)
    return


@app.cell
def _():
    r = np.random.randn(1000) * 100
    plt.hist(r, bins=60)
    plt.show()
    return


@app.cell
def _():
    rb = np.random.randint(low=0,high=2, size=(6,10))
    return (rb,)


@app.cell(hide_code=True)
def _(rb):
    mo.ui.matrix(rb,disabled=True)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## **Element-Wise Operations**
    """)
    return


@app.cell
def _():
    a = np.arange(10.)
    a
    return (a,)


@app.cell
def _(a):
    b = (np.sqrt(a**2 + 4**2))
    b
    return (b,)


@app.cell
def _(b):
    re_a = np.sqrt(b**2 - 4**2)
    re_a
    return (re_a,)


@app.cell
def _(a, b):
    a == b
    return


@app.cell
def _(a, re_a):
    a == re_a
    return


@app.cell
def _(a, re_a):
    a[a!= re_a]
    return


@app.cell
def _(a, re_a):
    for x,y in zip(a,re_a):
        print(x,y, x==y)
    return (x,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##**Summarizing Operations**
    """)
    return


@app.cell
def _(b):
    b.std()
    return


@app.cell
def _(b):
    b.mean()
    return


@app.cell
def _(b):
    b.min()
    return


@app.cell
def _(b):
    b.max()
    return


if __name__ == "__main__":
    app.run()
