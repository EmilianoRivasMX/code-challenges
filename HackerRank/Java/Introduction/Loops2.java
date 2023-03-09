/*
 * You are given q queries in the form of a, b, and n. 
 * For each query, print the series corresponding to the given a, b, and n values 
 * as a single line of  space-separated integers.
 * 
 * Series pattern: (a + 2^0 * b), (a + 2^0 * b + 2^1 * b), ..., (a + 2^0 * b + 2^1 * b + 2^n-1 * b)
 */

import java.util.Scanner;

public class Loops2 {
    public static void main(String[] args) {
        // Create a scanner for user input
        Scanner in = new Scanner(System.in);
        int q = in.nextInt();

        // Iterate the number of queries
        for(int i = 0; i < q; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            // Print the corresponding serie
            int serie = a;
            for(int j = 0; j < n; j++) {
                serie += Math.pow(2, j) * b;
                System.out.print(serie + " ");
            }
            System.out.println("");
        }
        in.close();
    }    
}
