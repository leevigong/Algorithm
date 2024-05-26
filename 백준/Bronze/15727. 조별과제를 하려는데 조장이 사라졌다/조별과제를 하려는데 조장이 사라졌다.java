import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        if (l%5 == 0){
            System.out.println(l/5);
        }
        else
            System.out.println(l/5+1);
    }
}