# rinobot-plugin-normalize


## Arguments:

In the extra args section of the rinobot automation config you can set the following parameters

Extra args:
```
--column=2 --algo=max
```

Column is which ever data column you want to normalize, and algo is either `sum` or `max`, to normaize
by the sum of every number in the column, or by the max number in the column.

## Example

Normalizes an axis of your data.

If your data looks like:

```
0 1
1 2
2 3
3 4
4 5
```

You can normalize any column by either its `sum` or its `max`,
here is `max` for the example data above, using `--column=2 --algo=max`

```
0 0.2
1 0.4
2 0.6
3 0.8
4 1.0
```
