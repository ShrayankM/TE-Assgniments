#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int data_b,parity_b,i=1,end_index;
	int array_p[20];
	int k=0;
	int three,not_one;
	int parity;
	int x;
	bool d = true;
	int jump,jump_count;
	bool check_count = true;
	int back_value;
	bool add_bit_one = true,add_bit_Gone = true;
	int input_data[20],got_data[100];
	int sent_parity[20],received_parity[20];
	int p=0;
	int received_data[100];
	int parities[200];
	for(int i=0;i<20;i++)
			array_p[i]=-1;
	for(int i=0;i<100;i++)
		got_data[i]=-1;
	cout<<"Enter the number of data bits \t";
	cin>>data_b;
	cout<<"Enter the data";
	for(int i=0;i<data_b;i++)
	{
		cin>>input_data[i];
	}
	while(d)
	{
		if(pow(2,i)>= data_b + i + 1)
		{
			parity_b=i;
			d=false;
		}
		i++;
	}
	end_index=data_b + parity_b;
	for(int i=end_index;i>0;i--)
	{
		for(int j=0;j<parity_b;j++)
		{
			if(i==pow(2,j))
			{
				check_count=false;
				break;
			}
		}
		if(check_count)
		{
			got_data[i]=input_data[k];
			k++;
		}
		check_count=true;
	}
	for(int i=end_index;i>=0;i--)
		cout<<got_data[i];
	cout<<"\n";
	for(int i=0;i<parity_b;i++)
	{
		jump=pow(2,i);
		x=pow(2,i);
		if(jump==1 && add_bit_one==true)
			{
				parities[x]=got_data[3];

				parity=got_data[3];
				three=3;
				add_bit_one=false;
			}
			else if(add_bit_Gone == true)
			{
				not_one=pow(2,i)+1;
				add_bit_Gone=false;
				back_value=not_one;
			}
			if(jump==1)
			{
				while(three+2<=end_index)
				{
					three=three+2;
					parity=parity^got_data[3];
				}
				cout<<"Parity"<<x<<"="<<parity<<"\n";
				sent_parity[p]=parity;
				p++;
				got_data[x]=parity;
			}
			else if(jump>1)
			{
				while(not_one<=end_index)
				{
					for(int j=0;j<parity_b;j++)
					{
						if((not_one) == pow(2,j))
						{
							not_one=not_one+jump;
							break;
						}
					}
					array_p[k]=got_data[not_one];
					k++;
					not_one++;
				}
				parity=array_p[0];
				for(int y=1;y<k;y++)
					parity=parity^array_p[y];
				cout<<"Parity"<<x<<"="<<parity<<"\n";
				sent_parity[p]=parity;
				p++;
				got_data[x]=parity;
			}
			cout<<"\n";
			add_bit_Gone=true;
			add_bit_one=true;
			k=0;
	}
	cout<<"\n";
	cout<<"Transmitted Data ";
	for(int i=end_index;i>0;i--)
			cout<<got_data[i];
		cout<<"\n";
//Received Part*********************
	cout<<"Enter the number of received data bits \t";
	cin>>data_b;
	cout<<"Enter the data";
	for(int i=data_b;i>0;i--)
	{
		cin>>received_data[i];
	}
	for(int i=0;i<20;i++)
		array_p[i]=-1;
/****************************************************/
	add_bit_one = true;
	add_bit_Gone = true;
	p=0;
	for(int i=0;i<parity_b;i++)
	{
		jump=pow(2,i);
		x=pow(2,i);
		if(jump==1 && add_bit_one==true)
		{
			parity=received_data[3];
			three=3;
			add_bit_one=false;
		}
		else if(add_bit_Gone == true)
		{
			not_one=pow(2,i)+1;
			add_bit_Gone=false;
			back_value=not_one;
		}
		if(jump==1)
		{
			while(three+2<=end_index)
			{
				three=three+2;
				parity=parity^got_data[3];
			}
			cout<<"Parity"<<x<<"="<<parity<<"\n";
			received_parity[p]=parity;
			p++;
		}
		else if(jump>1)
		{
			while(not_one<=end_index)
			{
				for(int j=0;j<parity_b;j++)
				{
					if((not_one) == pow(2,j))
					{
						not_one=not_one+jump;
						break;
					}
				}
				array_p[k]=received_data[not_one];
				k++;
				not_one++;
			}
			parity=array_p[0];
			for(int y=1;y<k;y++)
				parity=parity^array_p[y];
			cout<<"Parity"<<x<<"="<<parity<<"\n";
			received_parity[p]=parity;
			p++;
		}
		cout<<"\n";
		add_bit_Gone=true;
		add_bit_one=true;
		k=0;

	}
	int h;
	cout<<"Bit in binary";
	for(int i=0;i<parity_b;i++)
	{
		h=sent_parity[i]^received_parity[i];
		cout<<h;
	}
	cout<<"\n";
	int binary;
	long bin, dec = 0, rem, num, base = 1;
	cout<<"Please Enter Binary number";
	cin>>num;
	while (num > 0)
	{
		rem = num % 10;
		dec = dec + rem * base;
		base = base * 2;
		num = num / 10;
	}
	cout<<"Error Bit is"<<dec;
	return 0;
}

