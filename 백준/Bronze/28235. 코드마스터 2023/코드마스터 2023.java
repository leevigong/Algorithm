import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        if (name.equals("SONGDO")){
            System.out.println("HIGHSCHOOL");
        }
        else if (name.equals("CODE")){
            System.out.println("MASTER");
        }
        else if (name.equals("2023")){
            System.out.println("0611");
        }
        else if (name.equals("ALGORITHM")){
            System.out.println("CONTEST");
        }
    }
}
