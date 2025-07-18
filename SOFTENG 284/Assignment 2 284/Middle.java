import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Middle {
  public static void main(String[] args) {
    FastScanner in = new FastScanner();
    PrintWriter out = new PrintWriter(System.out);

    int m = in.nextInt();
    int count = 0;
    ArrayList<Integer> list = new ArrayList<>();
    while (count<m){
    int n = in.nextInt();
      if(n==1){
        int k = in.nextInt();
        list.add(k);
        count++;
        continue;
      }
      Collections.sort(list);
      int l = list.size();
      int n1 = (l)/2;
      out.println(list.get(n1));
      count++;
    }
    out.close();
  }

  static class FastScanner {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer("");

    String next() {
      while (!st.hasMoreTokens())
        try {
          st = new StringTokenizer(br.readLine());
        } catch (IOException e) {
        }
      return st.nextToken();
    }

    int nextInt() {
      return Integer.parseInt(next());
    }
  }
}
