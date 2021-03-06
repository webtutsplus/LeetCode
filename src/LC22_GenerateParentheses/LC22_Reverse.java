package LC22_GenerateParentheses;

import java.util.ArrayList;
import java.util.List;

public class LC22_Reverse {
    List<String> ans ;
    public List<String> generateParenthesis(int n) {


        ans  = new ArrayList<>();

        solve(n,n,"");

        return ans;

    }

    private void solve(int open,int closed,String op){

        if(open==0 && closed==0){
            ans.add(op);
        }

        if(open!=0){
            String op1 = op;
            op1 += "(";
            solve(open-1,closed,op1);
        }

        if(closed>open){

            String op2 = op;
            op2 += ")";
            solve(open,closed-1,op2);

        }



    }
}
