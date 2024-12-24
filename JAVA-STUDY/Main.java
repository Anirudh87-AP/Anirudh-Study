import java.util.* ;
class Main
{
    public static void main(String[] args)
    {
        Scanner SC = new Scanner(System.in);
        System.out.print("Enter the Integer(Whole Number) of Five Digits: ");
        int a = SC.nextInt();
        int b = a % 10;
        int c = (a % 100) - b;
        int d = (a % 1000) - c;
        int e = (a % 10000) - d;
        int SD = b + c + d + e;
        if (SD % 5 == 0)
        {
            if (SD % 3 == 0);
            {
                System.out.println("Divisible by both 3 and 5");
            }
            else
            {
                System.out.println("Divisible by 5");
            }
        }
        else if (SD % 3 == 0)
        {
            System.out.println("Divisible by 3 not by 5");
        } 
        else
        {
            System.out.println("Not divisible by 3 or 5")
        }
    } 
}