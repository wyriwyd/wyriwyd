Tutorial
--------

This is the tutorial for a totally awesome package. We haven't written
it yet, so instead we'll be demoing some bash tools.
Please run this from inside the `examples` subdirectory.

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

```output
kittens are great kittens
```

We should probably add some pictures or something as well.

Some commands don't have outputs, but in our tutorial syntax we use an
empty code block to indicate this.

```bash
touch unimportant_file
```

Some commands will need an input file to work on. Make sure this file exists 
inside the repo, and the path is correct.
```bash
cat cats.dat
```

```output
tiger
lion
cheetah
housecat
jaguar
Mr Mittens
```

You might also have a series of commands that are prerequisites to one command
running successfully and/or producing the expected output.
```bash
touch dogs.dat
echo catdog > dogs.dat
wc -l dogs.dat
```

```output
1 dogs.dat
```
