# CPP



string Solution::solve(string A, int B) {
    if(B==0)
        return A;
    int n=A.size();
    int a=stoi(A);
    int b=B;
    int max=0;
    for(int i=0; i<n-1;i++)
    {
        for(int j=i+1; j<n; j++)
        {
            string C=to_string(a);
            swap(C[i],C[j]);
            string ans=solve(C,b-1);
            int val=stoi(ans);
            if(val>max)
                max=val;
        }
    }
    return to_string(max);
}


# PYTHON3

def solve(A: str, B: int) -> str:
    max_val = [A]

    def helper(s, k):
        if k == 0:
            return
        n = len(s)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if s[j] > s[i]:  # Optimization: Only swap if it increases the number
                    lst = list(s)
                    lst[i], lst[j] = lst[j], lst[i]
                    new_s = ''.join(lst)
                    if new_s > max_val[0]:
                        max_val[0] = new_s
                    helper(new_s, k - 1)

    helper(A, B)
    return max_val[0]

