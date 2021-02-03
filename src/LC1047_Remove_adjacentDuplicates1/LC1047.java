package LC1047_Remove_adjacentDuplicates1;
import java.util.*;

public class LC1047 {
        public String removeDuplicates(String s) {
            //It keeps all the elements in the stack
            Stack<Character> stack = new Stack<>();

            for(int i=0;i<s.length();i++){

                char c = s.charAt(i);

                //If the top of the stack is equal to the current character we pop that element from the stack.
                if(!stack.isEmpty() && stack.peek()==c){
                    stack.pop();
                }
                //else we add that character into the stack
                else{
                    stack.add(c);
                }



            }
            //We will store the characters in an stringbuilder.
            StringBuilder sb = new StringBuilder("");


            while(!stack.isEmpty()){
                sb.append(stack.pop());

            }


            String x = String.valueOf(sb);

            //as we get the reverse output from the stack ,
            return reverse(x);
        }


        //Reverse a string
        private String reverse(String s){

            char[] ar = s.toCharArray();

            int left = 0;
            int right = ar.length-1;

            while(left<right){

                char c = ar[right];
                ar[right] = ar[left];
                ar[left] = c;

                left++;
                right--;

            }

            return new String(ar);

        }


}
