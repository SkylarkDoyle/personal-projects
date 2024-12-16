#include <iostream>
using namespace std;

/*
Given an array arr of integers, check if there exist two indices i and j such that :

    * i != j
    * 0 <= i, j < arr.length
    * arr[i] == 2 * arr[j]
*/

bool checkIfExist(int arr[], int size){

    // int len = sizeof(arr);
    // cout << arr;

    for(int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            //if i is not equal to j and position i in array is equal to 2 * position j in the array
            //then there is a even number in the array
            if(i != j && arr[i] == 2*arr[j]){
                return true;
            }
            
        }
       

    }
    return false;

};

int main()
{
    int arr[4] = {10, 5, 7, 9};
    int size = sizeof(arr) / sizeof(arr[0]);

    if(checkIfExist(arr, size)){
        cout << "True, i is exactly twice the value of j";
    }
    else{
        cout << "False, i is not exactly twice the value of j";
    }

    return 0;
}