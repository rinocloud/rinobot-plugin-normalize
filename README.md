# rinobot-plugin-normalize

Normalizes an axis of your data.

If your data looks like:

```
0 8
1 2
2 2
3 3
4 7
```

And you choose to shift the second column by -1 then the result will be:

```
0.0 7
1.4 1
2.4 1
3.3 2
4.1 6
...
...
```


## Arguments:

In the extra args section of the rinobot automation config you can set the following parameters

Extra args:
```
--column=2 --shift=-5
```

You can set all or none of these parameters.
