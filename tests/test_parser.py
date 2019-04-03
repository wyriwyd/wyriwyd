from wyriwyd.parser import parse_string


demo_doc = """
Tutorial
--------

This is the tutorial for a totally awesome package. We haven't written
it yet, so instead we'll be demoing some bash tools.

```bash
echo "cats are great cats" | sed 's/cat/kitten/'
```

```output
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

```bash
echo "cats are great cats" | sed 's/cat/kitten/g'
```

```output
kittens are great kittens
```

```bash
echo "cats are great cats" | sed 's/cat/kitten/g'
```

```
kittens are great kittens
```

```bash
echo "cats are great cats" | sed 's/cat/kitten/g'
```

```
kittens are great kittens
```

We should probably add some pictures or something as well.

"""


def test_parse_string():
    pairs = parse_string(demo_doc)
    assert len(pairs) == 5
    assert all(map(lambda x: len(x) == 2, pairs))
    assert pairs[0][0] == """echo "cats are great cats" | sed 's/cat/kitten/'"""
    assert pairs[0][1] == """kittens are great cats"""
    assert pairs[1][0] == """echo "cats are great cats" | sed 's/cat/kitten/g'"""
    assert pairs[1][1] is None
