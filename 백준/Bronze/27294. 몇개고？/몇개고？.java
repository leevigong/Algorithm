import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int s = sc.nextInt();
        String day;
        if (t<=11){
            day = "breakfast";
        }
        else if (12<=t && t<=16){
            day = "lunch";
        }
        else{
            day = "dinner";
        }

        if((s==1)||(!day.equals("lunch"))){
            System.out.println(280);
        }
        else if((s==0)&&(day.equals("lunch"))){
            System.out.println(320);
        }
    }
}
