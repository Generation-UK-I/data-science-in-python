# Introduction to Matplotlib

Matplotlib is the fundamental plotting library in Python for creating static, animated, and interactive visualizations. It's the foundation upon which many other Python visualization libraries (like Seaborn, Pandas plotting, and Plotly) are built.

It is used for:

- Analysing trends
- Comparing values
- Monitoring systems
- Presenting findings
- Debugging performance issues

## Installing Matplotlib

Matplotlib is not included in the Standard Python Library, but it can be installed using `pip`.

>**Optional**: Create a virtual environment with `python -m venv ./venv` then activate it with `.venv\Scripts\activate.ps1`

Install Matplotlib by running `pip install Matplotlib` in your terminal, then import it into your workspace just like any other module, however by convention we alias it as `pd`:

```python
import Matplotlib.pyplot as plt
```

## Why Matplotlib?

- Versatility: Create almost any type of plot imaginable
- Fine-grained control: Customize every aspect of your plots
- Integration: Works seamlessly with NumPy, Pandas, and SciPy
- Cross-platform: Works on Windows, macOS, Linux, and in web backends
- Publication-quality: Produce high-resolution figures for papers and presentations

### Architecture

Matplotlib has a three-layer architecture:

- Backend Layer: Handles rendering to various outputs (screen, files, etc.)
- Artist Layer: Everything you see (lines, text, ticks, etc.) is an Artist object
- Scripting Layer (pyplot): The interface most users interact with

### Anatomy of a Matplotlib Figure

Matplotlib graphs your data on Figures which are made of several parts:

- Figure: Think of the Figure as a blank canvas or a piece of paper. It's the top-level container that holds everything.
- Axes: Where the actual plotting happens. A Figure can contain multiple Axes objects.
- Axis: Handles the x-axis and y-axis, including limits, ticks, and labels.
- Ticks: the marks on the axes
- Labels: axis labels
- Title: the plot title
- Legend: labels for multiple lines or categories

Think of the Figure as a blank canvas or a piece of paper. It's the top-level container that holds everything.

## Creating a Plot

Line plots show trends over time.

```py
import matplotlib.pyplot as plt

cpu_usage = [40, 55, 70, 65, 80]

plt.plot(cpu_usage)
plt.show()
```

- `plot()`: draws the graph
- `show()`: renders it 
- The default x-axis is the `index` position

### Adding Labels and Title

A chart without labels is almost useless.

```py
plt.plot(cpu_usage)
plt.title("CPU Usage Over Time")
plt.xlabel("Time")
plt.ylabel("CPU %")
plt.show()
```
