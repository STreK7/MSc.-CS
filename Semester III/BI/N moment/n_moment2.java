import java.io.*;
import java.util.*;

class n_moment2 {

    public static void main(String args[]) {
        int n = 15;
        String stream[] = {"a", "b", "c", "b", "d", "a", "c", "d", "a", "b", "d", "c", "a", "a", "b"};
        int zero_moment = 0, first_moment = 0, second_moment = 0, count = 1, flag = 0;
        ArrayList<Integer> arrlist = new ArrayList();
        System.out.println("Arraylist elements are :: ");
        for (int i = 0; i < 15; i++) {
            System.out.print(stream[i] + " ");
        }
        Arrays.sort(stream);
	//Calculate Zeroth moment(calculates unique elements-raised to zero) 
        for (int i = 1; i < n; i++) {
            if (stream[i] == stream[i - 1]) {
                count++;
            } else {
                arrlist.add(count);
                count = 1;
            }

        }
    }
}
