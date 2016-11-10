# rinobot-plugin-normalize

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


## Options

## Options:

In the extra args section of the rinobot automation config you can set the following parameters

- algo [__required__]: either `sum` or `max`, to normalize by the sum of every number in the column, or by the max number in the column.
- cols: the columns to work on (see [Selecting columns and rows of data](https://docs.rinocloud.com/rinocloud-desktop/slicing_data.html))
- rows: the rows to work on
