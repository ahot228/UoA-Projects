import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Bipartite {
  private final int V;
  public Bipartite(int L) {
    V = L;
  }
  private boolean isBipartite(int G[][], int src){
    int colorArr[] = new int[V]; 
    for (int i = 0; i < V; ++i){
      colorArr[i] = -1; 
    }
    colorArr[src] = 1; 
    LinkedList<Integer>q = new LinkedList<Integer>(); 
    q.add(src); 
    while (q.size() != 0) { 
      int u = q.poll(); 
      if (G[u][u] == 1) 
        return false;  
      for (int v=0; v<V; ++v) { 
        if (G[u][v]==1 && colorArr[v]==-1) {
          colorArr[v] = 1-colorArr[u]; 
          q.add(v); 
        }else if (G[u][v]==1 && colorArr[v]==colorArr[u]) 
          return false; 
      } 
    } 
    return true; 
  }

  public static void main(String[] args) {
    int order = 1;
    String input = "";
    ArrayList<Integer> arr1 = new ArrayList<Integer>();

    Scanner scan = new Scanner(System.in);

    while (order != 0) {
      order = Integer.parseInt(scan.nextLine());
      if(order == 0){
        break;
      }
      int i = 0;
      Bipartite b = new Bipartite(order);
      int G[][] = new int[order][order];
      
      while(i < order){
        input = scan.nextLine();
        if (input.equals("")) {
          i++;
          continue;
        }
        String[] tokens = input.split(" ");
        int[] arr = new int[tokens.length];
       for (int j = 0; j < tokens.length; j++) {
          arr[j] = Integer.parseInt(tokens[j]);
        }
        for(int k = 0; k < order; k++){
          for(int l = 0; l < order; l++){
            for(int m = 0;m<tokens.length;m++){
              if(arr[m] == k && l == i){
               G[k][l] = 1;
              }
            }
          }
        }
        i++;
      }
      if(b.isBipartite(G, 0)){
        arr1.add(1);
      }else{
        arr1.add(0);
      }
    }
    for(int j = 0; j < arr1.size(); j++){
      System.out.println(arr1.get(j));
    }
    scan.close();

  }

}


