#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double entropy(vector<double> a)
{
	double sum = 0;
	for(auto x:a) sum+= x;

	double ans = 0;
	for(auto x:a) {
		double temp = (x/sum) * log2(x/sum);
		ans -= temp;
	}
	return ans;
}

int main()
{
	int n;
	vector<double> input;
	while(cin>>n){
		for(int i=0; i<n; i++){
			double temp;
			cin>>temp;
			input.push_back(temp);
		}
		cout<<"entropy: "<<entropy(input)<<endl;
		input.clear();
	}
}