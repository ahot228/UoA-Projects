import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Cycle {
  private final int V;
  private final List<List<Integer>> adj;
  
  public Cycle(int V)
    {
        this.V = V;
        adj = new ArrayList<>(V);
         
        for (int i = 0; i < V; i++)
            adj.add(new LinkedList<>());
    }


  private boolean isCyclicUtil(int i, boolean[] visited,boolean[] recStack){
        if (recStack[i])
            return true;
 
        if (visited[i])
            return false;
             
        visited[i] = true;
 
        recStack[i] = true;
        List<Integer> children = adj.get(i);
         
        for (Integer c: children)
            if (isCyclicUtil(c, visited, recStack))
                return true;
                 
        recStack[i] = false;
 
        return false;
    }
 
    private void addEdge(int source, int dest) {
        adj.get(source).add(dest);
    }
  private boolean isCyclic() {
    boolean[] visited = new boolean[V];
    boolean[] recStack = new boolean[V];
          
    // Call the recursive helper function to
    // detect cycle in different DFS trees
    for (int i = 0; i < V; i++)
        if (isCyclicUtil(i, visited, recStack))
            return true;

    return false;
  }

  public static void main(String[] args) {
    int order = 1;
    String input = "";

    Scanner scan = new Scanner(System.in);
    ArrayList<Integer> arr = new ArrayList<Integer>();

    while (order != 0) {
      order = Integer.parseInt(scan.nextLine());
      if(order == 0){
        break;
      }
      int i = 0;
      Cycle graph = new Cycle(order);

      while (i < order) {
        input = scan.nextLine();
        if (input.equals("")) {
          i++;
          continue;
        }
        String[] tokens = input.split(" ");
        int[] arr1 = new int[tokens.length];
        for (int j = 0; j < tokens.length; j++) {
          arr1[j] = Integer.parseInt(tokens[j]);
        }
        for(int k = 0; k < order; k++){
          for(int l = 0; l < order; l++){
            for(int m = 0;m<tokens.length;m++){
              if(arr1[m] == k && l == i){
                graph.addEdge(k, l);
              }
            }
          }
        }
        i++;
      }
      if(graph.isCyclic()){
        arr.add(1);
      }else{
        arr.add(0);
      }
    }
    for(int j = 0; j < arr.size(); j++){
      System.out.println(arr.get(j));
    }
    scan.close();

  }


}


