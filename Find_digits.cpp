#include <bits/stdc++.h>

using namespace std;

int findDigits(long long n)
{
    long long x=n;

    int count =0;

    while(x>0)
    {
        int t=x%10;

        if(t!=0 && n%t==0)
        {
            count++;
        }
        x/=10;
    }
    return count;
}

int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        long long n;
        cin>>n;
        cout<<findDigits(n)<<endl;
    }
}
