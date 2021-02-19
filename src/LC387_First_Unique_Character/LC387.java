package LC387_First_Unique_Character;
import java.util.*;

public class LC387 {
        public int firstUniqChar(String s) {
            //hashmap to store character frequency
            HashMap<Character, Integer> hashMap = new HashMap<>();

            for (int i = 0; i < s.length(); i++) {

                char c = s.charAt(i);

                //count the occurance of each character
                if (hashMap.containsKey(c))
                    hashMap.put(c, hashMap.get(c) + 1);
                else
                    hashMap.put(c, 1);

            }


            //Iterate through the string again.
            for (int i = 0; i < s.length(); i++) {


                char c = s.charAt(i);
                //If a characters occurance is 1 then we return the index
                if (hashMap.get(c) == 1)
                    return i;


            }

            //If no character has an occurance of 1 we return -1
            return -1;

        }
}
