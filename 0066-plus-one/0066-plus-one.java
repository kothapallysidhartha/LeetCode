class Solution {
    public int[] plusOne(int[] num) {
        int n = num.length;

        if (num[n - 1] + 1 != 10) {
            num[n - 1]++;
            return num;
        }

        int carry = 1;
        for (int i = n - 1; i >= 0; i--) {
            num[i] += carry;
            carry = num[i] / 10;
            num[i] %= 10;

            if (carry == 0) {
                break;
            }
        }
        if (carry == 1) {
            int[] result = new int[n + 1];
            result[0] = 1;
            System.arraycopy(num, 0, result, 1, n);
            return result;
        }

        return num;
    }
}