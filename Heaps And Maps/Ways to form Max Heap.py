####    PYTHON3




MOD = 10**9+7

class Solution:
    # @param A : integer
    # @return an integer
    
    def comb(self,r,n) :
        if 2*r > n : 
            return self.comb(n-r,n)
        c = 1
        for i in range(r) :
            c = c*(n-i)//(i+1)
        return c
    
    def solve(self, A):
        ans,h = [1,1], 0
        for n in range(2,A+1) :
            if 2<<h <= n :
                h += 1
            m = n-(1<<h)+1
            l = (1<<(h-1))-1 + min(m,1<<(h-1))
            r = (1<<(h-1))-1 + max(0,m-(1<<(h-1)))
            ans.append((self.comb(l,n-1)*ans[l]*ans[r])%MOD)
        return ans[A]

            


####    JAVA



public class Solution {
    static final int MOD = 1000000007;
    static long[] fact = new long[1001];
    static long[] invFact = new long[1001];
    static boolean initialized = false;

    // Precompute factorials and inverse factorials modulo MOD
    private void init() {
        if (initialized) return;

        fact[0] = invFact[0] = 1;
        for (int i = 1; i < 1001; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }
        invFact[1000] = modInverse(fact[1000]);
        for (int i = 999; i >= 1; i--) {
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
        }

        initialized = true;
    }

    // Compute modular inverse using Fermat's Little Theorem
    private long modInverse(long x) {
        return modPow(x, MOD - 2);
    }

    private long modPow(long base, int exp) {
        long result = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }

    // nCr % MOD
    private long comb(int r, int n) {
        if (r > n) return 0;
        return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
    }

    public int solve(int A) {
        init();
        long[] ans = new long[A + 2]; // extra space for 0 and 1
        ans[0] = 1;
        ans[1] = 1;
        int h = 0;

        for (int n = 2; n <= A; n++) {
            if ((2L << h) <= n) h++;

            int m = n - ((1 << h) - 1);
            int left = ((1 << (h - 1)) - 1) + Math.min(m, (1 << (h - 1)));
            int right = n - 1 - left;

            long val = comb(left, n - 1);
            val = (val * ans[left]) % MOD;
            val = (val * ans[right]) % MOD;
            ans[n] = val;
        }

        return (int) ans[A];
    }
}


                    #####

public class Solution {
    static final int MOD = 1000000007;
    static long[] fact = new long[1001], invFact = new long[1001];
    static boolean done = false;

    void init() {
        if (done) return;
        fact[0] = invFact[0] = 1;
        for (int i = 1; i <= 1000; i++) fact[i] = (fact[i - 1] * i) % MOD;
        invFact[1000] = power(fact[1000], MOD - 2);
        for (int i = 999; i >= 1; i--) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
        done = true;
    }

    long power(long a, int b) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) == 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            b >>= 1;
        }
        return res;
    }

    long comb(int r, int n) {
        if (r > n) return 0;
        return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
    }

    public int solve(int A) {
        init();
        long[] dp = new long[A + 2];
        dp[0] = dp[1] = 1;
        int h = 0;

        for (int n = 2; n <= A; n++) {
            if ((2L << h) <= n) h++;
            int m = n - (1 << h) + 1;
            int left = (1 << (h - 1)) - 1 + Math.min(m, 1 << (h - 1));
            int right = n - 1 - left;

            dp[n] = (((comb(left, n - 1) * dp[left]) % MOD) * dp[right]) % MOD;
        }

        return (int) dp[A];
    }
}




####      C++


#define MOD 1000000007
#define MAX 1001

long long fact[MAX], invFact[MAX];
bool precomputed = false;

// Fast exponentiation for modular inverse
long long power(long long a, int b) {
    long long res = 1;
    while (b) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

// Precompute factorials and inverse factorials
void init() {
    if (precomputed) return;
    fact[0] = invFact[0] = 1;
    for (int i = 1; i < MAX; i++) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 1; i--) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    precomputed = true;
}

// Compute C(r, n) % MOD
long long comb(int r, int n) {
    if (r > n) return 0;
    return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
}

// Main function
int Solution::solve(int A) {
    init();
    vector<long long> dp(A + 2, 0);
    dp[0] = dp[1] = 1;
    int h = 0;

    for (int n = 2; n <= A; n++) {
        if ((2LL << h) <= n) h++;
        int m = n - (1 << h) + 1;
        int left = (1 << (h - 1)) - 1 + min(m, 1 << (h - 1));
        int right = n - 1 - left;

        dp[n] = (((comb(left, n - 1) * dp[left]) % MOD) * dp[right]) % MOD;
    }

    return dp[A];
}













