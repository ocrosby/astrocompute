import marimo

__generated_with = "0.11.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # The APC Math Module
        """
    )
    return


@app.cell
def _():
    from astrocompute.library.apc_math import (
        Angle,
        AngleFormat,
        AngleSerializer,
    )

    return Angle, AngleFormat, AngleSerializer


@app.cell
def _(AngleSerializer):
    ngs = AngleSerializer()
    return (ngs,)


@app.cell
def _(Angle, AngleFormat, mo, ngs):
    mo.md(
        r"""
        ## The Angle Serializer
        """
    )
    print(ngs.serialize(Angle(12.3456, AngleFormat.Dd)))
    print(ngs.serialize(Angle(12.3456, AngleFormat.DMM)))
    print(ngs.serialize(Angle(12.3456, AngleFormat.DMMm)))
    print(ngs.serialize(Angle(12.3456, AngleFormat.DMMSS)))
    print(ngs.serialize(Angle(12.3456, AngleFormat.DMMSSs)))
    return


if __name__ == "__main__":
    app.run()
