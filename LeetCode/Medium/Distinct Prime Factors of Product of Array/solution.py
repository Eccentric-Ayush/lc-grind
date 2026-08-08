class Solution:
    def get_prime(self, n):
        factors = []
        
        # 1. Handle factor 2 separately (allows step size of 2 in loop)
        while n % 2 == 0:
            factors.append(2)
            n //= 2
            
        # 2. Check odd numbers up to sqrt(n)
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
            
        # 3. If n is still greater than 2, the remaining n is prime
        if n > 2:
            factors.append(n)
        return factors

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        new_set = []
        for i in nums:
            new_set.extend(self.get_prime(i))

        return len(set(new_set))
