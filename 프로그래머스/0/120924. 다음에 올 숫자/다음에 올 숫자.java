class Solution {
  public int solution(int[] common) {
    int answer = 0;
    
    int a = common[1] - common[0];
    int b = common[2] - common[1];
    
    if (a==b) {
      answer = common[common.length-1]+a;
    } else {
      int c = b / a;
      answer = common[common.length-1]*c;
    }
    return answer;
  }
}