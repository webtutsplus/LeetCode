class LC1736 {
public:
    string maximumTime(string time) {
        string ans="00:00";
        //"?5:?5"=>"15:55"
        //index0
        if(time[0] == '?')
        {
            if(time[1] == '?') time[0]='2';
            else if(time[1] >= '4') time[0]='1';
            else time[0] = '2';
        }
        //index 1
        if(time[0]=='0' || time[0]=='1')
        {
            if(time[1]=='?') time[1]='9';
        }
        else
        {
            if(time[1]=='?') time[1]='3';
        }
        //index3
        if(time[3] == '?')
        {
            time[3] = '5';
        }
        //index4
        if(time[4] == '?')
        {
            time[4]='9';
        }
        return time;
    }
};