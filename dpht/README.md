# DPHT (Double Pendulum Hash Table)

Hash table class that implements DPHF as its hash function.

Probably much, much slower than just searching a list, but a proof-of-concept.


```python
table = Dpht(10)
print(table)
```

```
Index   Value
0               -
1               -
2               -
3               -
4               -
5               -
6               -
7               -
8               -
9               -
```

```python
names = ["Aleksi", "Aleks", "Alex", "Aleksandr", "Alexander"]
for name in names:
    table.append(name)
print(table)
```

```
Index   Value
0               Alex
1               Aleks
2               -
3               Aleksi
4               -
5               Alexander
6               Aleksandr
7               -
8               -
9               -
```

```python
lookup_name = "Aleksi"
index = table.lookup(lookup_name)
print(f"{lookup_name} found at index {index}.")
```

```
Aleksi found at index 3.
```