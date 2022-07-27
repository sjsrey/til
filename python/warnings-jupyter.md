# Turning warnings off for a cell in Jupyter

Sometimes, particularly in a teaching context, it is useful to be able to turn off warnings for particular cells.
This can be done with:

```
%%capture --no-display
df[df.A > 5]['B'] = 4
```

[Source](https://softhints.com/turn-off-warnings-jupyterlab-jupyter-notebook/)
