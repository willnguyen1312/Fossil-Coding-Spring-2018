#include <bits/stdc++.h>

using namespace std;
int m;
int main() {

	#ifndef ONLINE_JUDGE
	// freopen("5.in", "r", stdin);
	freopen("8.in", "w", stdout);
	#endif
	int n = 1000;
	cout << n << endl;

	while(n--) {
		cout << (m = rand() % 50 + 1) << endl;
		for(int i = 0; i <  m; i++) {
			cout << rand()%11<< ' ';
		}
		cout << endl;
	}
}