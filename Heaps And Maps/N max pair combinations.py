####   C++


vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    priority_queue<pair<int, pair<int, int> > > hp;
	set<pair<int, int> > S;
	int n = A.size();
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());

	hp.push(make_pair(A[n-1]+B[n-1], make_pair(n-1, n-1)));
	S.insert(make_pair(n-1, n-1));

	vector<int> ans;
	int k=n;
	while(k--){
		pair<int, pair<int, int> > top = hp.top();
		hp.pop();
		ans.push_back(top.first);
		int L = top.second.first;
		int R = top.second.second;
		
		if( R>0 && L>=0  && S.find(make_pair(L,R-1)) == S.end() ){
			hp.push(make_pair(A[L]+B[R-1], make_pair(L,R-1)));
			S.insert(make_pair(L,R-1));
		}
		if( R>=0  && L>0 && S.find(make_pair(L-1, R))==S.end()){
			hp.push(make_pair(A[L-1]+B[R], make_pair(L-1,R)));
			S.insert(make_pair(L-1, R));
		}
	}
	return ans;
}




#####   PYTHON3



import heapq

class Solution:
    def solve(self, A, B):
        n = len(A)
        A.sort()
        B.sort()

        max_heap = []
        visited = set()

        # Start from the largest possible sum
        i = j = n - 1
        heapq.heappush(max_heap, (-(A[i] + B[j]), i, j))
        visited.add((i, j))

        result = []

        for _ in range(n):
            val, i, j = heapq.heappop(max_heap)
            result.append(-val)

            # Move in B
            if j - 1 >= 0 and (i, j - 1) not in visited:
                heapq.heappush(max_heap, (-(A[i] + B[j - 1]), i, j - 1))
                visited.add((i, j - 1))

            # Move in A
            if i - 1 >= 0 and (i - 1, j) not in visited:
                heapq.heappush(max_heap, (-(A[i - 1] + B[j]), i - 1, j))
                visited.add((i - 1, j))

        return result



#####    JAVA





import java.util.*;

public class Solution {
    public ArrayList<Integer> solve(ArrayList<Integer> A, ArrayList<Integer> B) {
        int n = A.size();
        Collections.sort(A);
        Collections.sort(B);

        PriorityQueue<PairSum> maxHeap = new PriorityQueue<>();
        Set<String> visited = new HashSet<>();

        int i = n - 1, j = n - 1;
        maxHeap.add(new PairSum(A.get(i) + B.get(j), i, j));
        visited.add(i + "," + j);

        ArrayList<Integer> result = new ArrayList<>();

        for (int count = 0; count < n; count++) {
            PairSum current = maxHeap.poll();
            result.add(current.sum);

            int x = current.i;
            int y = current.j;

            // Move to (x, y - 1)
            if (y - 1 >= 0 && !visited.contains(x + "," + (y - 1))) {
                maxHeap.add(new PairSum(A.get(x) + B.get(y - 1), x, y - 1));
                visited.add(x + "," + (y - 1));
            }

            // Move to (x - 1, y)
            if (x - 1 >= 0 && !visited.contains((x - 1) + "," + y)) {
                maxHeap.add(new PairSum(A.get(x - 1) + B.get(y), x - 1, y));
                visited.add((x - 1) + "," + y);
            }
        }

        return result;
    }

    class PairSum implements Comparable<PairSum> {
        int sum, i, j;

        public PairSum(int sum, int i, int j) {
            this.sum = sum;
            this.i = i;
            this.j = j;
        }

        @Override
        public int compareTo(PairSum other) {
            return Integer.compare(other.sum, this.sum); // max heap
        }
    }
}




