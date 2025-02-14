#include<iostream>
#include<string>
#include<cctype>
using namespace std;
int main() {
    string A;
    cin>>A;
    string strongPassword = "";

    if(islower(A[0])) {
        strongPassword +=toupper(A[0]);
    } 
    int len = A.length();

    for(int i=1; i<len; i++) {
        if(A[i] == 's') strongPassword+='$'; 
        else if(A[i] == 'i') strongPassword+='!'; 
        else if(A[i] == 'o') strongPassword+="()";   
        else strongPassword +=A[i];
    }
   strongPassword+='.';
   cout<<strongPassword;

    return 0;
}