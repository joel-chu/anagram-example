/**
 * This is an example (Js doesn't really need this)
 * but we are going to use the same idea and port to
 * other not-so-advance lanauge such as Java piece of shit
 */
const PENDING = "pending"
const RESOLVED = "resolved"
const REJECTED = "rejected"

function MyPromise(fn) {
  const that = this
  that.state = PENDING
  that.value = null

  that.resolvedCallbacks = []
  that.rejectedCallbacks = []

  function resolve(value) {
    setTimeout(() => {
      if (that.state === PENDING) {
        that.state = RESOLVED
        that.value = value
        that.resolvedCallbacks.map(cb => cb(that.value))
      }
    }, 0)
  }

  function reject(value) {
    setTimeout(() => {
      if (that.state === PENDING) {
        that.state = REJECTED;
        that.value = value;
        that.rejectedCallbacks.map(cb => cb(that.value))
      }
    },0) // add setTimeout trick to off a stack
  }

  /*
    we could totally create a factory method to create the above two

  function factory(newState, calls) {
    return function(value) {
      if (that.state === PENDING) {
        that.state = newState;
        that.value = value;
        that[calls].map(cb => cb(that.value))
      }
    }
  }
  */
  // now run the top fn method
  try {
    fn(resolve, reject)
  } catch(e) {
    reject(e)
  }
}

// create the then method
MyPromise.prototype.then = function(onFullfilled, onRejected) {
  const that = this

  onFullfilled = typeof onFullfilled === 'function' ? onFullfilled : v => v
  onRejected = typeof onRejected === 'function' ? onRejected : r => {
    throw r
  }
  // why they use if not switch?
  if (that.state === PENDING) {
    // Update: return a new Promise2
    return (promise2 = new MyPromise((resolve, reject) => {
      that.resolvedCallbacks.push(() => {
        try {
          const x = onFullfilled(that.value)
          resolutionProcedure(promise2, x, resolve, reject)
        } catch(e1) {
          reject(e1)
        }
      })
      that.rejectedCallbacks.push(() => {
        try {
          const x = onRejected(that.value)
          resolutionProcedure(promsie2, x, resolve, reject)
        } catch(e1) {
          reject(e1)
        }
      })
    }))
    /*
    V.1
    that.resolvedCallbacks.push(onFullfilled)
    that.rejectedCallbacks.push(onRejected)
    */
  }

  if (that.state === RESOLVED) {
    return (promise2 = new MyPromise((resolve, reject) => {
      setTimeout(() => {
        try {
          const x = onFullfilled(that.value)
          resolutionProcedure(promise2, x, resolve, reject)
        } catch(e2) {
          reject(e2)
        }
      }, 0)
    }))
    //V.1  onFullfilled(that.value)
  }

  if (that.state === REJECTED) {
    return (promise2 = new MyPromise((resolve, reject) => {
      setTimeout(() => {
        try {
          const x = onRejected(that.value)
          resolutionProcedure(promise2, x, resolve, reject)
        } catch(e3) {
          reject(e3)
        }
      },0)
    }))
    //V.1 onRejected(that.value)
  }
  // finally the method that allow this method to get use in different places
  function resolutionProcedure(promise2, x, resolve, reject) {
    if (promise2 === x) {
      return reject((new TypeError('Error')))
    }
    if (x instanceof MyPromise) {
      x.then(function(value) {
        resolutionProcedure(promise2, value, resolve, reject)
      }, reject)
    }
    // the remaining code to check if one promise is already fullfilled or rejected before continue
    let called = false
    if (x !== null && (typeof x === "object" || typeof x === "function")) {
      try {
        let then = x.then
        if (typeof then === "function") {
          then.call(
            x,
            y => {
              if (called) return
              called = true
              resolutionProcedure(promise2, y, resolve, reject)
            },
            e => {
              if (called) return
              called = true
              reject(e)
            }
          )
        } else {
          resolve(x)
        }
      } catch(e) {
        if (called) return
        called = true
        reject(e)
      }
    } else {
      resolve(x)
    }
  }
}
