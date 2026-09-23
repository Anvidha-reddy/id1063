#include<stdio.h>
int days_elapsed(int day, int month)
{  
      int m={31,28,31,30,31,30,31,31,30,31,30,31};
      int days=day;	
      for(int i=1;i<month;i=++)
	{
        days=days+m[i-1];
        return days;
	}
int main()
{
	printf("Enter day,month");
	scanf("%d, %d",&day &month);
int	d=days elapsed(day,month);
	printf("days: ",d);
	return 0;
}
