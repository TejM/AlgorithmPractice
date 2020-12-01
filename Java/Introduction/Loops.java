import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
             
            int sum = a; 
            for (int j=0; j < n-1; j++) {
                sum += (int)(Math.pow(2, j)*b);
                System.out.print(sum + " ");
            }
            
            // This is so that we can avoid the whitespace for the last print value
            sum += (int)(Math.pow(2, n-1)*b);
            System.out.println(sum);
        }
        in.close();
    }
}
