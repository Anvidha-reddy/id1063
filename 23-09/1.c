#include<stdio.h>
#include<math.h>
double rms(double a[],double n)
{  
    double sum=0.0;
    for(int i=0;i<n;i++)
{
	sum=a[i]*a[i]+sum;
}
     double rms=0;
     rms=pow(sum/n,1/2);
     return rms;
}


int main()
{
   int n;
   scanf("%d", &n);  
   double a[n];
   for(int i=0;i<n;i++)     
{
        scanf("%lf", &a[i]);                       }
	rms(a,n);
	printf("%.2f", rms(a,n));
	}

