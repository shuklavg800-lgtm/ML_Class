#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<vector<int>> takeinput(int n) {
    vector<vector<int>> arr(n, vector<int>(2));

    for (int i = 0; i < n; i++) {
        cout << "Enter x" << i + 1 << ": ";
        cin >> arr[i][0];
        cout << "Enter y" << i + 1 << ": ";
        cin >> arr[i][1];
    }
    return arr;
}

float linear_regression(const vector<vector<int>>& arr, int x, int n) {
    float sum_xy = 0;
    float sum_x = 0;
    float sum_y = 0;
    float sum_x_sq = 0;

    for (int i = 0; i < n; i++) {
        sum_xy += arr[i][0] * arr[i][1];
        sum_x += arr[i][0];
        sum_y += arr[i][1];
        sum_x_sq += arr[i][0] * arr[i][0];
    }

    // dividing the values to obtain the mean s: 
    float x_bar = sum_x / n;
    float y_bar = sum_y / n;
    float xy_bar = sum_xy / n;
    float x_sq_bar = sum_x_sq / n;

    float m = (xy_bar - x_bar * y_bar) / (x_sq_bar - x_bar * x_bar);
    float c = y_bar - m * x_bar;

    return m * x + c;
}

int main() {
    int n = 0;
    cout << "Enter the number of data points: ";
    cin >> n;

    vector<vector<int>> arr = takeinput(n);

    int x = 0;
    cout << "Enter the value of X to predict Y: ";
    cin >> x;
    float result = linear_regression(arr, x, n);
    cout << "Predicted Y = " << result << endl;
    return 0;
}
