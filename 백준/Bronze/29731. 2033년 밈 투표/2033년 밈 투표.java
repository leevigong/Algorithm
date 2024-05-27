import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<String> list = new ArrayList<>();
        list.add("Never gonna give you up");
        list.add("Never gonna let you down");
        list.add("Never gonna run around and desert you");
        list.add("Never gonna make you cry");
        list.add("Never gonna say goodbye");
        list.add("Never gonna tell a lie and hurt you");
        list.add("Never gonna stop");

        String a = "No";
        sc.nextLine();

        for (int i = 0; i <n; i++) {
            String s = sc.nextLine();
            if (!list.contains(s)) {
                a = "Yes";
            }
        }
        System.out.println(a);
    }
}
