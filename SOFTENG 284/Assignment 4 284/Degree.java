class Degree{
    public static void main(String[] args){
        Digraph G = new Digraph(new In(args[0]));
        int s = Integer.parseInt(args[1]);
        BreadthFirstDirectedPaths bfs = new BreadthFirstDirectedPaths(G, s);
        int max = 0;
        for(int v = 0; v < G.V(); v++){
            if(bfs.hasPathTo(v)){
                int length = bfs.distTo(v);
                if(length > max) max = length;
            }
        }
        StdOut.println(max);
    }
    public BreadthFirstDirectedPaths(Digraph G, int s){
        marked = new boolean[G.V()];
        edgeTo = new int[G.V()];
        distTo = new int[G.V()];
        bfs(G, s);
    }
}