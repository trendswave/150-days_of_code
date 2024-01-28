# Fixed error in fizzbuzz logic

 In the `fizzbuzz(n)` function, the logic for checking multiples of both 3 and 5 is incorrect. The condition `(i % 3) == 0` should be checked before the condition `(i % 5) == 0` because the first condition will match numbers that are multiples of both 3 and 5. So, you need to swap the order of the conditions