import java.*;

class add
{
	static native int my_Add(int a,int b);
	static native int my_Sub(int a,int b);
	static native int my_Mul(int a,int b);
	static native int my_Div(int a,int b);
	static
	{
		System.loadLibrary("add");
	}
	public static void main(String args[])
	{
		int value;
		add object = new add();
		int a=10,b=20;
		value = object.my_Add(a,b);
		System.out.println("Addition is "+value);
		
		a=20;b=10;
		value = object.my_Sub(a,b);
		System.out.println("Subraction is "+value);

		value = object.my_Mul(a,b);
		System.out.println("Multiplication is "+value);

		value = object.my_Div(a,b);
		System.out.println("Division is "+value);

	}
}
