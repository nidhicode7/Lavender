import java.util.Scanner;
class Main{
public static void main(String[] args){
    System.out.println("Enter number:");
    Scanner Sc=new Scanner(System.in);
    int n,sum=0;
    n=Sc.nextInt();
    while(n!=0){
        sum+=n%10;
        n=n/10;
    }
    System.out.println("Sum of digits:"+sum);
}
}
