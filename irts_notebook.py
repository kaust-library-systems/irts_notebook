import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    IRTS Notebook
    =============

    Notebook for IRTS functions and libraries
    """
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    import requests as rq
    import xml.etree.ElementTree as ET
    return ET, mo, rq


@app.cell
def _(mo):
    mo.md(
        r"""
    # Harvest

    Harvest the publication from all sources registered.

    ## Arxiv

    1. Get list of IDs from the database.
    2. Query `arxiv` for the ID.
    """
    )
    return


@app.cell
def _(rq):
    url="http://export.arxiv.org/api/query?search_query=0801.2310&start=0&max_results=1"
    result = rq.get(url)
    return (result,)


@app.cell
def _(result):
    if result.status_code == 200:
        content = result.content.decode("utf-8")
    return (content,)


@app.cell
def _(content):
    print(content)
    return


@app.cell
def _(ET, content):
    metadata = ET.fromstring(content)
    return (metadata,)


@app.cell
def _(metadata):
    for tag in metadata:
        print(tag.tag, tag.attrib)
    return


@app.cell
def _(metadata):
    entry = metadata.find('{http://www.w3.org/2005/Atom}entry')
    return (entry,)


@app.cell
def _(entry):
    for ii in entry:
        print(ii)
    return


@app.cell
def _(entry):
    id = entry.find('{http://www.w3.org/2005/Atom}id')
    authors = entry.findall('{http://www.w3.org/2005/Atom}author')
    print(f"We found {len(authors)} authors for {id.text}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
