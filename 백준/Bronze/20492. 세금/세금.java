import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int one = (int) (n*0.78);
        int two = (int) (n*0.80 + n*0.2*0.78);
        System.out.printf("%d %d", one, two);
    }
}