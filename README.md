# Python recursion

> First of all, you can do this in `ANY` language you want. but i'm going to use some python imports rh.

So, **what's a recursion?**

`Recursion is the process in which a function calls itself directly or indirectly.` [Geek for Geeks](https://www.geeksforgeeks.org/recursion/)

When you call the same function inside itself, you have a recursion. Let me show you an example:

```python
# It's a basic example, some people uses recursion to calculate factorial of some number

def factorial(n):
    if n == 1:
        return 1 # ends function (otherwise it'll be an infinite loop)
    else:
        return factorial(n - 1) * n # how does it work?
```

> If you don't know what's factorial, [Here's some help](https://en.wikipedia.org/wiki/Factorial)

## How does it work?

When you return the same function with the parameter (originally an integer) minus one, you are just 'rewriting' the function inside itself, for example, let's pretend `N` is `3`:

```python
def factorial(n): # 3
    if n == 1:
        return 1
        
    return factorial(n - 1) * n
```

> Obs: You **have** to insert some value, otherwise it's going to loop through it infinitely.

It's going to return: ```factorial(2)```, because of `(3 - 1)`. The memory is going to store: `6`, because `(3 - 1) * 3[n]` is equal to **6**.


Then, the function runs again with `2` as parameter, and it's going to return `factorial(1)`, that returns `1`. <br>
**So we have in the memory:**

* 6 `3 x 2`
* 1 `2 x 1`
* 1 `1 x 1`

And the function is going to do what's supposed to do, a `multiplication`! <br>
`6 x 1 x 1 = 6`, **that's the result.**

---

### Another example

```python
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
        
    return fibonacci(n - 1) + fibonacci(n - 2)
```

> If you have doubts about fibonnaci sequence, [Here's some help](https://en.wikipedia.org/wiki/Fibonacci_number)

**So, here we have a more advanced example, but it works the same way.**

If we try to run this with `fibonacci(15)`, it's going to return 610, that's the result we want!
![Result we want](https://imgur.com/687YkQI.png) <br>

**But we have a `big` problem.** <br>

If we try to run this with a "large" number like `fibonacci(50)`, terminal will display it with `5 to 10 seconds` time delay.

### So, why is this happening?

It's strange, but it has a solution! <br>

It's happening because the function is going to storage `all` the values that it has already returned, for example:

`Based on fibonacci sequence`, when we call it with 5 for example, it stores: `1, 1, 2, 3 and 5`. <br>

If we do this with a large number like `fibonacci(250)`, it's going to store `1, 1, 2, 3, 5, 8, 13...` until it reaches the 250th position, because `fibonacci(4)` is the result of `fibonacci(2) + fibonacci(3)`, `fibonacci(3)` is the result of `fibonacci(2) + fibonacci(1)` and so on. Computer really thinks he has to store it, and it consumes `a lot` of memory. **That's why terminal has that time delay**.

### How can we fix this with Python?

To solve this we have to cache the values, so the function doesn't have to do it for us. To help us we have a builtin Python tool that's called [functools](https://docs.python.org/3/library/functools.html), and it has a lot of things inside of it, we're going to use only one called [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache). It basically caches all the function results for us.

#### How to use

It's simple, you just have to import it:

```python
from functools import lru_cache
```

And then you place it above your function:
> Note: Not EVERY recursive function is going to have this delay, such as factorial.

```python
from functools import lru_cache

@lru_cache(maxsize = 1000) # maxsize is the "max stack" the function can have.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
        
    return fibonacci(n - 1) + fibonacci(n - 2)
    
print( fibonacci(250) ) # 7896325826131730.... with 0 delay.
```

## Thank you!

That's it. I hope you learned a little bit from this. If you don't, you can see this other links that i think it's going to help you:

* [Geek for Geeks](https://www.geeksforgeeks.org/recursion/)
* [Programiz](https://www.programiz.com/python-programming/recursion) `It also has a lot of courses about python, worth seeing!`
* [Joe James](https://www.youtube.com/watch?v=wMNrSM5RFMc) `YouTube`
