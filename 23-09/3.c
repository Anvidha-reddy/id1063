#include <stdio.h>
int runlength(int a[], int n, int i)
{ 
	if(i < 0 || i >= n || a[i] == 0)
	{
		return 0;//invalid conditions
	}
	int count=0;
	for(int j=i;a[j]==1;j++)
	{
		count++;
		return count;//counting how many consecutive 1s
	}
}
int main() {
    int n, k;//input n,k
    scanf("%d %d", &n, &k);
    // Input array elements of length n
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
      int count=runlength(a,n,k);
	    printf("outout:%d",k+count);
	    return 0;
}
