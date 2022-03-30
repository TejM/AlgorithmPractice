import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
       return occurrenceMap(a).equals(occurrenceMap(b));
    }
    
    static java.util.Map<String, Integer> occurrenceMap(String a) {
        java.util.Map<String, Integer> map = new java.util.HashMap<String, Integer>();
        
        for (String letter : a.split("")) {
            map.put(letter.toLowerCase(), map.getOrDefault(letter.toLowerCase(), 0) + 1);
        } 
        
        return map;
    }    

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
