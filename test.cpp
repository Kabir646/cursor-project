#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> nextLargerElement(vector<int> arr) {
        int n = arr.size();
       stack<int>st;
       vector<int> nge;
       for(int i = n-1 ; i>=0;i--){
        if(st.empty()){
            nge[i]=-1;
            st.push(arr[i]);
        }
        else{
            while(!st.empty()){
                if(st.top()>arr[i]){
                    nge[i]=st.top();
                    break;
                }
                else{
                    st.pop();
                }
            }
            if(st.empty()){
            nge[i]=-1;
            st.push(arr[i]);
        }
        }
       }
       return nge;
    }
};
