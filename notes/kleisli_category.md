## Kleisli Category

### Overview
The Kleisli category is related to types and functions, particularly in the context of function composition with side effects.
It provides a structured way to manage effects while keeping functions pure.

### Problem Statement
We have a library of pure functions, but a new requirement demands an audit trail.
The challenge is to introduce logging without introducing side effects.

#### Issue with Side Effects
```cpp
string log = "";

bool negate(bool x) {
    log += "not!";
    return !x;
}
```
- The global variable `log` introduces a side effect.
- Side effects increase complexity due to hidden interactions.
- There is no indication from the function signature that `negate` modifies `log`.

#### A More Local Approach
```cpp
pair<bool, string> negate(bool x, string log) {
    return make_pair(!x, log + "Non");
}
```
- The function now explicitly takes and returns a log.
- However, `negate` is now responsible for handling logging, violating **Separation of Concerns**.

#### Further Improvement
```cpp
pair<bool, string> negate(bool x) {
    return make_pair(!x, "Non");
}
```
- This approach eliminates explicit log handling in the function.
- However, log concatenation is now the caller's responsibility.

### Solution: Function Composition with Embellishments
We modify how we compose functions so that they return a **pair** (value, log), shifting the responsibility of log concatenation into the composition function.

#### Function Composition for Embellished Functions
```cpp
template <class A, class B, class C>
function<pair<C, string>(A)> compose(
    function<pair<B, string>(A)> f,
    function<pair<C, string>(B)> g) {

    return [f, g](A x) {
        auto p1 = f(x);
        auto p2 = g(p1.first);
        return make_pair(p2.first, p1.second + p2.second);
    };
}
```
- This ensures logging is handled naturally within composition.
- The approach generalizes to any **monoid** (e.g., logs, sums, lists).

### Kleisli Arrows and Monads
- Kleisli arrows allow composition of functions that return **embellished** values.
- Many useful embellishments exist beyond logging, such as error handling (`Maybe`), asynchronous computations (`Future`), and state transformations.
- This structure works because the embellishment forms a **monad**.

### Conclusion
Using the Kleisli category and function composition with embellishments, we can structure side-effectful computations while maintaining purity and composability.


