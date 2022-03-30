//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
	public static void main(String []argh)
	{
        Map<String,Integer> phoneNumberMap = new HashMap<>();         
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			int phone=in.nextInt();
			in.nextLine();
            phoneNumberMap.put(name, phone);
		}
		while(in.hasNext())
		{
			String s=in.nextLine();
            String output = phoneNumberMap.containsKey(s) ? 
                (s + "=" + phoneNumberMap.get(s)) : "Not found";
            System.out.println(output);
		}
	}
}



