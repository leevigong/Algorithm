import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            if(s.length() >=6 && s.length()<=9){
                System.out.println("yes");
            }
            else{
                System.out.println("no");
            }
        }
    }
}
