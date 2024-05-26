import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger sum = new BigInteger("0");
        for (int i =0; i<5; i++) {
            BigInteger a = sc.nextBigInteger();
            sum = sum.add(a);
        }
        System.out.println(sum);
    }
}