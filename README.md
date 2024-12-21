# Piping

Use object-oriented "method access" to call builtin functions taking an iterable as input.

Mimics shell piping, inspired by Java streams.

## Example usage

```py
from pipe import Pipe

iterable = (
    Pipe(range(40))
        .filter(lambda x: x % 2 == 0)
        .map(lambda x: x // 2)
        .reversed()
)
for i in iterable:
    print(i)  # 19, 18, 17 ... 2, 1, 0

hello_sum = (
    Pipe("hello, world!")
        .map(ord)
        .sum()
)
print(hello_sum)  # 1193
```
