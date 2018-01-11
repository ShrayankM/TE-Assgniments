import java.*;
import java.util.Scanner;
class test
{
	
	static
	{
		System.loadLibrary("cal");
	}
	public native int add(int a,int b);
	public native int sub(int a,int b);
	public native int mul(int a,int b);
	public native int div(int a,int b);
	public native float my_sqrt(int a);
	public native double my_sin(int a);
	public native double my_cos(int a);
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
		int value;
		int angle;
		double value2;
		test obj = new test();
		int choice=1;
		System.out.println("Calculator");
		
		
		while(choice!=5)
		{
			System.out.println("1)Addition 2)Subraction 3)Multiplication 4)Division 6)Sqrt 7)Sin 8)Cos 5)Exit");
			choice = input.nextInt();
			switch(choice)
			{
				case 1:
					value = obj.add(10,20);
					System.out.println("Addition is "+value);
					break;
					
				case 2:
					value = obj.sub(20,10);
					System.out.println("Subraction is "+value);
					break;
				
				case 3:
					value = obj.mul(10,20);
					System.out.println("Multiplication is"+value);
					break;
					
				case 4:
					value = obj.div(20,10);
					System.out.println("Division is "+value);
					break;
					
				case 5:
					System.out.println("Exit");
					break;
					
				case 6:
					value2 = obj.my_sqrt(25);
					System.out.println("Sqrt of 25 is"+value2);
					break;
					
				case 7:
					System.out.println("Enter Angle");
					angle = input.nextInt();
					value2 = obj.my_sin(angle);
					System.out.println("Sine of"+ angle+"degree is"+value2);
					break;
					
				case 8:
					System.out.println("Enter Angle");
					angle = input.nextInt();
					value2 = obj.my_cos(angle);
					System.out.println("Cos of"+ angle+"degree is"+value2);
					break;
				default:
					System.out.println("Please Enter Correct Option");
					break;	
			}	
		}
		
		
		
	}
}
