import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Pattern {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String pattern = br.readLine();
    String text = br.readLine();
    int occurences = 0;
    int M = pattern.length();
    int N = text.length();
    int i, j;
    int p = 0; // hash value for pattern
    int t = 0; // hash value for txt
    int h = 1;

    for (i = 0; i < M - 1; i++)
            h = (h * 256) % 101;
 
        // Calculate the hash value of pattern and first
        // window of text
        for (i = 0; i < M; i++) {
            p = (256 * p + pattern.charAt(i)) % 101;
            t = (256 * t + text.charAt(i)) % 101;
        }
 
        // Slide the pattern over text one by one
        for (i = 0; i <= N - M; i++) {
 
            // Check the hash values of current window of
            // text and pattern. If the hash values match
            // then only check for characters one by one
            if (p == t) {
                /* Check for characters one by one */
                for (j = 0; j < M; j++) {
                    if (text.charAt(i + j) != pattern.charAt(j))
                        break;
                }
 
                // if p == t and pat[0...M-1] = txt[i, i+1,
                // ...i+M-1]
                if (j == M)
                    occurences++;
            }
 
            // Calculate hash value for next window of text:
            // Remove leading digit, add trailing digit
            if (i < N - M) {
                t = (256 * (t - text.charAt(i) * h)
                     + text.charAt(i + M))
                    % 101;
 
                // We might get negative value of t,
                // converting it to positive
                if (t < 0)
                    t = (t + 101);
            }
  }
  int counter = occurences;
  System.out.println(counter);
}
}
