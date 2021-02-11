class LC202 {
public:
    int convert(int n){
        int ans = 0;
        while(n){

            ans += pow(n%10, 2);
			n/=10;

        }
        return ans;
    }

    bool isHappy(int n) {
        bool map[1000];

        memset(map, 0, sizeof(map));

        n = convert(n);

        while(!map[n]){
			map[n] = true;
            if(n == 1)
                return true;
			n = convert(n);
        }

        return false;
    }
};