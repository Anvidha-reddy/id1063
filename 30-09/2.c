#include <stdio.h>
int main()
{
	int n,m;
	scanf("%d %d",&n, &m);
	int a[n][m];
	//taking matrix input
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=m;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	int b[n][m];
	for(int i=1;i<=n;i++) 
	{                                                         for(int j=1;j<=m;j++)                             {
	//checking if it is a mine
		if(a[i][j]==1)
		{
			b[i][j]=-1;
		}
	//checking if it is an empty cell
		else if(a[i][j]==0)
		{
			int count=0;
			for(int k=i-1;k<=n;
		}
		else
		{
			printf("Enter valid input")
		}
