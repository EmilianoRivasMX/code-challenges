/*  
 * Given an integer, N, print its first 10 multiples. 
 * Each multiple N x i (Where 1 <= i <= 10) should be printed on a new line in form: N x i = result.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Loops1 {
    public static void main(String[] args) throws IOException {
        // Create a reader and read the input
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine().trim());
        bufferedReader.close();

        // Print first 10 multiples
        for(int i = 1; i <= 10; i++) {
            int result = N * i;
            System.out.println(N + " x " + i + " = " + result);
        }
    }
}
