import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) {
        LocalDateTime date = LocalDateTime.now();
        
        System.out.println(date.getYear());
        System.out.println(date.getMonthValue());
        System.out.println(date.getDayOfMonth());
    }
}