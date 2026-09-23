#include<stdio.h>
#include<string.h>
int firstStable(double a[], int n, double tolerance){
	if(a.len()!=n)
{
	printf("Enter exact number of entries");
	}
{
	for(int i=0;i<n;i++)
{
	if(a[i+1] - a[i]| <= tolerance){
		return i;}
}       else
{
	return -1;
}
}
int main()
{
	int n;
	double a[],tolerance;
	printf("Enter n: ");
	scanf("%d",$n);
	printf("Enter the readings: ");
	for(int i=0;i<n;i++)
	{
	scanf("%lf",&a[i]);
	}
	printf("Enter tolerance: ")
	scanf("%lf",&tolerance);
	printf("%d",firstStable(a,n,tolerance));
	return 0;
	}

