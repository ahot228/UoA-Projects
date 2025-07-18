import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
//import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

 
public class MaxDist {
	
	public static void main(String[] args) {
    FastScanner in = new FastScanner();
 		PrintWriter out = new PrintWriter(System.out);

    int t = in.nextInt();
    for (int i = 0; i < t; i++) {
      int n = in.nextInt();
      int k = in.nextInt();

      int a[] = new int[n];
      for (int j = 0; j < n; j++) a[j] = in.nextInt();
      out.println(solve(a, k));
    }

    out.close();
	}

  public static int solve(int a[], int k) {
    List<int[]> subsets = new ArrayList<>();
    List<Integer> distances = new ArrayList<Integer>();
  int[] s = new int[k];                  // here we'll keep indices 

  if (k <= a.length) {
    // first index sequence: 0, 1, 2, ...
    for (int i = 0; (s[i] = i) < k - 1; i++);  
    subsets.add(getSubset(a, s));
    for(;;) {
        int i;
        // find position of item that can be incremented
        for (i = k - 1; i >= 0 && s[i] == a.length - k + i; i--); 
        if (i < 0) {
            break;
        }
        s[i]++;                    // increment this item
        for (++i; i < k; i++) {    // fill up remaining items
            s[i] = s[i - 1] + 1; 
        }
        subsets.add(getSubset(a, s));
    }
  }
for(int i = 0; i < subsets.size(); i++) {
  int[] subset = subsets.get(i);
  int min = Integer.MAX_VALUE;
  for(int j = 1; j < subset.length; j++) {
    //the minimum distance between any two elements in the subset
    if(min>Math.abs(subset[j] - subset[j-1])){
      min = Math.abs(subset[j] - subset[j-1]);
    }
  }
  distances.add(min);
}
// return the maximum of the minimum distances
return distances.stream().mapToInt(v -> v).max().getAsInt();
}
static int[] getSubset(int[] a, int[] subset) {
  int[] result = new int[subset.length]; 
  for (int i = 0; i < subset.length; i++)
    result[i] = a[subset[i]];
  return result;
}

  static class FastScanner {
      BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st=new StringTokenizer("");

      String next() {
        while (!st.hasMoreTokens())
          try { 
            st=new StringTokenizer(br.readLine());				              
          } catch (IOException e) {}
        return st.nextToken();
      }
      
      int nextInt() {
        return Integer.parseInt(next());
      }
  }
}

