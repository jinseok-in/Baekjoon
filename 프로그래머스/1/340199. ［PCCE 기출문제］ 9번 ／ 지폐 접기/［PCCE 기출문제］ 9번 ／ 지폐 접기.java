import java.util.Collections;

class Solution {
  public int solution(int[] wallet, int[] bill) {
      int answer = 0;
      
      while ((max(wallet) < max(bill)) || (min(wallet) < min(bill))) {
          if (bill[0] > bill[1]) {
              bill[0] = bill[0]/2;              
          } else {
              bill[1] = bill[1]/2;
          }
          answer += 1;
      }
      
      return answer;
  }
    public static int min(int[] array) {
        int min = array[0];
        for (int i : array) {
            if (i < min) {
                min = i;
            }
        }
        return min;
    }
    public static int max(int[] array) {
        int max = array[0];
        for (int i : array) {
            if (i > max) {
                max = i;
            }
        }
        return max;
    }
}
