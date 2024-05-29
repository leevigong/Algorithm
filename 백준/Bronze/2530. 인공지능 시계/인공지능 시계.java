import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); // 시
        int b = sc.nextInt(); // 분
        int c = sc.nextInt(); // 초
        int d = sc.nextInt(); // 필요한 시간(초)

        int hour;
        int min ;
        int sec ;

        if (d < 3600){
            hour = a;
            min = b+d/60;
            sec = c+d%60;
        }
        else{
            hour = a + d/3600;
            min = b + (d%3600)/60;
            sec = c + (d%3600)%60;
        }

        if(sec >= 60) {
            min = min + sec / 60;
            sec = sec - (sec / 60) * 60;
        }
        if (min >= 60){
            hour = hour + min/60;
            min = min - (min/60)*60;
            sec = sec - (sec/60)*60;
        }
        if (hour >= 24){
            hour = hour - (hour/24)*24;
        }

        System.out.printf("%d %d %d", hour, min, sec);
    }
}
