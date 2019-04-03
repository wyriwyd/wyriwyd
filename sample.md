Tutorial
--------

This is the tutorial for a totally awesome package. We haven't written
it yet, so instead we'll be demoing some bash tools.

```bash
echo "cats are great cats" | sed 's/cat/kitten/'
```

```
kittens are great cats
```

By default `sed` only deals with the first match. To match all case we
append a trailing *g*.

```bash
echo "cats are great cats" | sed 's/cat/kitten/g'
```

```
kittens are great kittens
```

We should probably add some pictures or something as well.

