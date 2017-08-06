#include <iostream>

using namespace std;

int main()
{


    int di[10] = {0,0,0,0,0,0,0,0,0,0};
    int ci[10] = {0,0,0,0,0,0,0,0,0,0};
    int vectorai[10] = {15,47,71,111,123,152,166,226,310,320};
    int vectorsi[10] = {43,36,34,30,38,40,31,29,36,30};

    int i=0;
    while (i< 10)
    {
        int ai,si;
        ai = vectorai[i];
        if (ai < ci[i-1])
        {
            di[i] = ci[i-1]-ai;
        }
        else
        {
            di[i] = 0;
        }
        si = vectorsi[i];
        ci[i] = ai + di[i] +si;
        i++;
    }
    cout<<"di = "<<"[";
    for (i=0; i<10; i++)
    {
        cout<<di[i]<<",";
    }
    cout<<"]";

    cout<<endl;

    cout<< "ci = "<<"[";
    for (i=0; i<10; i++)
    {
        cout<<ci[i]<<",";
    }
    cout<<"]";
    return 0;
}

