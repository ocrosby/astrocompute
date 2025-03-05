import marimo

__generated_with = "0.11.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from astrocompute.library.apc_vecmat3d import Vec3D
    return (Vec3D,)


@app.cell
def _(mo):
    mo.md("# The APC VecMath3D Module")
    return


@app.cell
def _(mo):
    mo.accordion(
        {
            "Creating a new 3 dimensional Vector": mo.md("my_vector = Vec3D(1,2,3)"),
            "Adding two 3 dimensional vectors": mo.md(r"""
            v1 = Vec3D(1,2,3)
            v2 = Vec3D(4,5,6)
            v3 = v1 + v2
            print(v1)
            print(v2)
            print(v3)
            """),
            "Door 3": mo.md(
                "![goat](https://images.unsplash.com/photo-1524024973431-2ad916746881)"
            ),
        }
    )
    return


@app.cell
def _(Vec3D):
    v1 = Vec3D(1,2,3)
    v2 = Vec3D(4,5,6)
    v3 = v1 + v2
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v3}")
    return v1, v2, v3


if __name__ == "__main__":
    app.run()
