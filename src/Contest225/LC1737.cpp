class LC1737 {
public:
    //make a less than b
    int make(string a, string b)
    {
        int local = INT_MAX;
        for(char ch='b'; ch<='z'; ch++)
        {
            //all characters in a are < ch
            //all characters in b are >= ch
            int temp = 0;
            for(char c:a)if(!(c<ch))temp++;
            for(char c:b)if(!(c>=ch))temp++;
            local = min(local, temp);
        }
        return local;
    }
    int minCharacters(string a, string b) {
        int ans = INT_MAX;
        ans = min(make(a,b), make(b,a));
        for(char ch='a'; ch<='z'; ch++)
        {
            int total = a.length()+b.length();
            for(char c : a) if(c == ch) total--;
            for(char c : b) if(c == ch) total--;
            ans = min(ans, total);
        }
        return ans;
    }
};