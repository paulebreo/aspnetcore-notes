
## Fibonacci - dynamic programming
source: educative.io - https://www.educative.io/collection/page/5668639101419520/5633779737559040/5744017589403648
```javascript
const calculateFibonacci = function(n) {
  const dp = [0, 1];
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
};

console.log(`5th Fibonacci is ---> ${calculateFibonacci(5)}`);
console.log(`6th Fibonacci is ---> ${calculateFibonacci(6)}`);
console.log(`7th Fibonacci is ---> ${calculateFibonacci(7)}`);
```