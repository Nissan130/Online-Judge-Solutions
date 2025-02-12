#include<iostream>
using namespace std;

int main() {
    int n;
    int numbers[100];
    cin>>n;
    for(int i=0; i<n; i++) {
        cin>>numbers[i];
    }

    int flag = 0;
    for(int i=0; i<n-1; i++) {
        if(numbers[i]>numbers[i+1]) {
            flag = 1;
        }
    }
    if(flag == 0) 
    {
        cout<<"Yes"<<endl;
    }
    else {
        cout<<"No"<<endl;
    }
    
    return 0;
}