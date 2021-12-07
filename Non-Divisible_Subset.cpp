#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;


int main()
{
    int n,k;
    cin>>n>>k;

    int count[k]={0};

    for(int i=0;i<n;i++)
    {
        int a;
        cin>>a;

        count[a%k]++;

    }


    int max=0;

    for(int i=0;i<=(k/2);i++)
    {

        if(i==0 || i==k-i)
        {
            if(count[i]>0)
            max++;
        }
        else
        {
            if(count[i]>=count[k-i])
            {
                max+=count[i];
            }
            else
            {
                max+=count[k-i];
            }

        }


    }
            cout<<max;

    return 0;
}
