class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i,l=s.length(),res=0,left=-1;
        vector <int> dict(256,-1);
        for (i=0;i<l;i++)
        {
            if (dict[s[i]]>left)
                left=dict[s[i]];
            dict[s[i]]=i;
            res=max(res,i-left);
        }
        return res;
    }
};
