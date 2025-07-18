import java.util.Scanner;

public class Reverse {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int order = 1;
    while(order != 0){
    order = Integer.parseInt(scan.nextLine());
    if (order == 0){
      System.out.println(0);
      break;
    }
    int i = 0;
    int[][] arr1 = new int[order][order];
    while (i < order) {
      String input = scan.nextLine();
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
              arr1[k][l] = 1;
            }
          }
        }
      }
      i++;
    }
    int count = 0;
    System.out.println("\n"+order);
    for(int o = 0; o < order; o++){
      for(int p = 0; p < order; p++){
        if(arr1[o][p] == 1){
          if(count>0){
            System.out.print(" ");
          }
          System.out.print(p);
          count++;
        }
        if(p == order-1&&o != order-1){
          count = 0;
          System.out.println();
        }
      }
    }
    }
    scan.close();
  }
}
