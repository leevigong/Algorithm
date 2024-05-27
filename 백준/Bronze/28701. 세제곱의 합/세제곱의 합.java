import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r1 = 0;
        int r2;
        int r3 = 0;
        for (int i = 1; i <= n; i++) {
            r1 += i;
            r3 += i*i*i;
        }
        r2 = r1*r1;
        System.out.println(r1);
        System.out.println(r2);
        System.out.println(r3);
    }
}
