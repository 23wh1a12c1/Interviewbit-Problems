

int Solution::colorful(int A) 
{
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    string s = to_string(A);
    map<long long, bool> mp;
    
    for(auto i=0; i<s.size(); i++)
    {
        long long mul = 1;
        
        for(auto j=i; j<s.size(); j++)
        {
            mul *= (long long)(s[j]-'0');
        
            if(mp.find(mul) != mp.end())
                return 0;
            
            mp[mul] = true;
        }
    }
    
    return 1; //O(n^2), O(n)
    
}



