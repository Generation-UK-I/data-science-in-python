# Introduction to Data Science in Python

This guide is intended to follow on from the Introduction to Python course, and acts as an accompaniment for learners pursuing a data-science program; it is also an optional component for people on other programs looking to extend their skills.

Three core tools used by almost all data scientists are `numpy`, `pandas`, and `matplotlib`.

These tools are closely related and integrate seamlessly, however each has specific functions and can be used individually.

## NumPy

NumPy is the Foundation, and provides fast numerical computing capabilities. It provides:

- Fast, memory‑efficient arrays
- Vectorised mathematical operations
- Tools for generating sequences, random numbers, matrices, etc.

Almost everything in scientific Python depends on NumPy because it replaces slow Python loops with fast C‑based operations.

## Pandas

Pandas uses NumPy internally; Every Pandas Series is essentially a NumPy array with labels; Every DataFrame column is built on top of NumPy arrays.

So NumPy is the engine that powers Pandas’ performance.

When using Pandas we work with:

- Series (labelled 1D data)
- DataFrames (labelled 2D tables)

Pandas includes tools for:

- loading data (CSV, Excel, SQL…)
- cleaning and transforming data
- filtering and grouping
- summarising and aggregating

## Matplotlib

Matplotlib is the visualisation layer that draws:

- line charts
- bar charts
- scatter plots
- histograms
- box plots
- and much more

## A Simple Analogy
Imagine you’re cooking a meal:

- NumPy is your raw ingredients (fast, basic building blocks)
- Pandas is your kitchen (tools for organising, preparing, and combining ingredients)
- Matplotlib is the plating and presentation (turning the final dish into something you can show others)

Each layer depends on the one below it, and together they form a complete workflow.

---

Find tutorials for each of these libraries below:

[Introduction to Numpy](/numpy/intro_numpy.md)  
[Introduction to Pandas](/pandas/intro_pandas.md)  
[Introduction to Matplotlib](/matplotlib/intro_matplotlib.md)
