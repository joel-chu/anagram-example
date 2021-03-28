# One possible solution to the `stackoverflow` problem

If you have run the program several times, you might encounter the famous `stackoverflow` error.
Basically, its too much calculation to do, your machine ran out of memory.

This is why we only limit the maximum letters long to 7.
Even that it could have to calculate at least 5,040 times;
It could be more because the random generator might came up with the same combination.

To illustrate the problem, you can try the follow simple example (I was running this on a AMD 3500 4 cores 8 thread with 16GB ram machine)

```js
const max = 100000

function recursion1(count = 0) {
  if (count === max) {
    return 'done'
  }
  ++count
  return recursion1(count)
}

console.time('r1')
const result = recursion1()
console.log(result)
console.timeEnd('r1')
```

The result is:

```sh
...
RangeError: Maximum call stack size exceeded
...
```

What we could do is by wrapper the inner recursive call in a `setTimeout`

```js

function recursion1(count = 0) {
  if (count === max) {
    return 'done'
  }
  ++count
  return setTimeout(() => {
    return recursion1(count)
  }, 0)
}
```

But wait, if you run the example above, there won't be any output at all.
Because `setTimeout` will not return anything from the inner function call.

To get around this problem, we need to restructure the function with `Promise`

```js
const max = 100000
function recursionInner(count = 0, _resolver) {
  if (count === max) {
    return _resolver('done') // this return just terminate the execution
  }
  setTimeout(() => {
    count++
    recursionInner(count, _resolver)
  }, 0)
}

function recursionOutter() {
  return new Promise(resolver => {
    recursionInner(0, resolver)
  })
}

console.time('r2')
recursionOutter()
  .then(result => {
    console.log(result)
    console.timeEnd('r2')
  })

```

Now you recursion function should run without that error.
What happened is, when you use the `setTimeout` even with a 0 mil second,
node.js will put that call on a stack, and clear the last stack before continue. Instead of what happened early, too many calls in one stack.
