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

Some commands don't have outputs, but in our tutorial syntax we use an
empty code block to indicate this.

```bash
touch unimportant_file
```
```
```
