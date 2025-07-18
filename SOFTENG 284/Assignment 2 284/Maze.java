import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Maze {
  int n;
  int[] parent;
  int[] rank;
  ArrayList<Integer> list = new ArrayList<>();
  public static void main(String[] args) {
    FastScanner in = new FastScanner();
    PrintWriter out = new PrintWriter(System.out);

    int n = in.nextInt();
    int m = in.nextInt();
    int count = 0;
    int[][] arr = new int[n][n];
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
       arr[i][j] = j*n+i;
      }
    }
    Maze maze = new Maze();
    maze.n = n;
    maze.parent = new int[n*n];
    maze.rank = new int[n*n];
    maze.makeSet();
    while (count<m){
      int a = in.nextInt();
      int b = in.nextInt();
      if(!maze.isConnected(a,b)){
        maze.union(a,b);
      }else{
        maze.list.add(a+b*b);
      }
      count++;
    }
    maze.printmaze(arr);
    out.close();
  }
  void makeSet(){
    for (int i = 0; i < n*n; i++) {
      parent[i] = i;
    }
  }
  int findrep(int x){
    if(parent[x] != x) {
      parent[x]=findrep(parent[x]);
    }
    return parent[x];
  }
  boolean isConnected(int x,int y){
    return findrep(x) == findrep(y);
  }
  void union(int x, int y){
    int xRoot = findrep(x), yRoot = findrep(y);
    if(rank[xRoot] < rank[yRoot])
      parent[xRoot] = yRoot;
    else
      parent[yRoot] = xRoot;
    if(rank[xRoot] == rank[yRoot]){
      rank[xRoot] = rank[xRoot] + 1;
    }
  }
  void printmaze(int[][] arr){
    int i;
    int j;
    String s = "";
    for (i = 0; i < n; i++) {
      s = s + "+-";
    }
    s = s + "+\n|";
    // Print the maze interior.
    for (j = 0; j < n; j++) {
      // Print a row of cells and vertical walls.
      for (i = 0; i < n-1; i++) {
        if (isConnected(arr[i][j],arr[i+1][j])&&(!list.contains(arr[i][j]+arr[i+1][j]*arr[i+1][j]))) {
          s = s + "  ";
        } else {
          s = s + " |";
        }
      }
      s = s + " |\n+";

      if (j < n - 1) {
        // Print a row of horizontal walls and wall corners.
        for (i = 0; i < n; i++) {
          if (isConnected(arr[i][j],arr[i][j+1])&&(!list.contains(arr[i][j]+arr[i][j+1]*arr[i][j+1]))) {
            s = s + " +";
          } else {
            s = s + "-+";
          }
        }
        s = s + "\n|";
      }
    }
    for (i = 0; i < n; i++) {
      s = s + "-+";
    }
    System.out.println(s);
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
