![](Images/empty-labs-logo-wide.png)

# Desk Cycle

This is a health monitoring project dedicated to visualizing progress on my stationary bike exercise using the [Desk Cycle](https://thedeskcycle.com/).

## Conda environment

When setting up the project, consider using a conda environment to isolate the required packages.

1.Set up jupyter for conda environment ([sauce](https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook))

```commandline
pip install jupyter ipykernel
```
```commandline
python -m ipykernel install --user --name desk-cycle --display-name "desk-cycle"
```

2. Install required packages to conda
```commandline
conda install anaconda::pandas
conda install conda-forge::matplotlib
```