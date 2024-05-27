import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float w = sc.nextFloat();
        float h = sc.nextFloat();
        System.out.printf("%.1f", w*h*0.5);
    }
}
