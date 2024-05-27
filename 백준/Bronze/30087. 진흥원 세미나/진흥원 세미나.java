import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<String, String> map = new HashMap<>();
        map.put("Algorithm", "204");
        map.put("DataAnalysis", "207");
        map.put("ArtificialIntelligence", "302");
        map.put("CyberSecurity","B101");
        map.put("Network", "303");
        map.put("Startup", "501");
        map.put("TestStrategy", "105");

        for (int i = 0; i < n; i++) {
            String key = sc.next();
            System.out.println(map.get(key));
        }
    }
}
