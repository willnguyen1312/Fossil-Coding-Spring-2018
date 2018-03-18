#include <bits/stdc++.h>

using namespace std;
int t, n, a, m;

int main() {
	freopen("7.in", "r", stdin);
	freopen("7.out", "w", stdout);
	cin >> t;

	while (t--) {
		cin >> n >> a >> m;
		int cheap = INT_MAX;
		
		int price;
		for(int i = 0; i < m; i++) {
			cin >> price;
			cheap = min(cheap, price);
		}

		if(cheap == 0)
			cout << n << endl;
		else
			cout << max(0, min(a/cheap - 1, n)) << endl;
	}

	return 0;
}