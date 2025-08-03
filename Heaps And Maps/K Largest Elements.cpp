###   C++

vector<int> Solution::solve(vector<int> &A, int B) {
    vector<int>ans;
    if(A.size()<B){
        return ans;
    }
    priority_queue<int> pq;
    for(int i = 0;i<A.size(); i++){
        pq.push(A[i]);
    }
    for(int i = 0; i<B; i++){
        ans.push_back(pq.top());
        pq.pop();
    }
    return ans;
}




######


vector<int> Solution::solve(vector<int> &A, int B) {
    if(B==A.size())return A;
    priority_queue<int,vector<int>,greater<int> >pq;
    for(int i=0;i<B;i++)
        pq.push(A[i]);
    for(int i=B;i<A.size();i++)
    {
        if(pq.top()<A[i])
        {
            pq.pop();
            pq.push(A[i]);
        }
    }
    vector<int>ans;
    while(pq.empty()==false)
    {
        ans.push_back(pq.top());
        pq.pop();
    }
    return ans;
}
