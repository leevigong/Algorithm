import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int sum = a + b + c;

        if(sum==180){
            if (a==b) {
                if (b == c) {
                    System.out.println("Equilateral");
                }
                else{
                    System.out.println("Isosceles");
                }
            }
            else if ((b==c)||(a==c)){
                System.out.println("Isosceles");
            }
            else{
                System.out.println("Scalene");
            }
        }
        else{
            System.out.println("Error");
        }

    }
}
