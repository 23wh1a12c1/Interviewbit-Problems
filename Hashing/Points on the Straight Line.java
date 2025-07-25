#######     C++


// https://www.interviewbit.com/problems/points-on-the-straight-line/

int Solution::maxPoints(vector<int> &A, vector<int> &B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    if(A.size() == 0 || B.size() == 0){
        return 0;
    }
    
    unordered_map<double, int> myMap;
    int sol = 1;
    for(int i = 0; i < A.size(); i++){
        int duplicate = 1;
        int vertical = 0;
        for(int j = i+1; j < A.size(); j++){
            if(A[i] == A[j]){
                if(B[i] == B[j]){
                    duplicate++;
                }
                else{
                    vertical++;
                }
            }
            else{
                double slope = 0.0;
                double x = A[j] - A[i];
                double y = B[j] - B[i];
                if(B[j] != B[i]){
                    slope = (1.0 * (y/x));
                }
                if(myMap.find(slope) != myMap.end()){
                    myMap[slope]++;
                }
                else{
                    myMap[slope] = 1;
                }
            }
        }
        auto it = myMap.begin();
        while(it != myMap.end()){
            int t = it->second;
            if((t + duplicate) > sol){
                sol = t + duplicate;
            }
            it++;
        }
        if((vertical + duplicate) > sol){
            sol = vertical + duplicate;
        }
        myMap.clear();
    }
    
    return sol;
}





############    PYTHON3











###########    JAVA



import java.util.*;

public class Solution {
    public int maxPoints(ArrayList<Integer> A, ArrayList<Integer> B) {
        if (A == null || B == null || A.size() == 0 || B.size() == 0)
            return 0;

        int n = A.size();
        int maxPoints = 1;

        for (int i = 0; i < n; i++) {
            Map<String, Integer> slopeMap = new HashMap<>();
            int duplicate = 1;
            int vertical = 0;

            for (int j = i + 1; j < n; j++) {
                if (A.get(i).equals(A.get(j))) {
                    if (B.get(i).equals(B.get(j))) {
                        duplicate++;
                    } else {
                        vertical++;
                    }
                } else {
                    int dx = A.get(j) - A.get(i);
                    int dy = B.get(j) - B.get(i);
                    int gcd = gcd(dy, dx);

                    dx /= gcd;
                    dy /= gcd;

                    // Normalize direction (important to avoid (-1,2) vs (1,-2))
                    if (dx < 0) {
                        dx = -dx;
                        dy = -dy;
                    }

                    String slopeKey = dy + "/" + dx;
                    slopeMap.put(slopeKey, slopeMap.getOrDefault(slopeKey, 0) + 1);
                }
            }

            int currMax = vertical;
            for (int count : slopeMap.values()) {
                currMax = Math.max(currMax, count);
            }

            maxPoints = Math.max(maxPoints, currMax + duplicate);
        }

        return maxPoints;
    }

    // Helper to calculate gcd
    private int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
