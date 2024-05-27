import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 지하철까지 걸어가는 시간
        int a = sc.nextInt(); // 버스 오는 시간
        int b = sc.nextInt(); // 지하철 오는 시간


        if (b>a){
            System.out.println("Bus");
        }
        else if (b<a){
            System.out.println("Subway");
        }
        else{
            System.out.println("Anything");
        }
    }
}
