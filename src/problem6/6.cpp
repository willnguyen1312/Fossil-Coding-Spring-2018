#include <bits/stdc++.h>

using namespace std;
int t, n, m;
string digits[] = {"khong","mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"};

int main() {
	freopen("6.in", "r", stdin);
	freopen("6.out", "w", stdout);
	cin >> t;

	while (t--) {
		cin >> m;
		int n = abs(m);
		if(m < 0) cout << "am ";

		if (n >= 1000) { //1234
			int a = n/1000;
			int b = n%1000/100;
			int c = n%100/10;
			int d = n%10;

			cout << digits[a] << " nghin ";

			cout << digits[b] << " tram ";

			if(c == 0)
				cout << "le ";
			else if(c == 1) 
				cout << "muoi ";
			else
				cout << digits[c] << " muoi ";

			if(d == 5) cout << "lam";
			else if (d != 0)
				cout << digits[d];

		} else if (n >= 100) {
			int b = n/100;
			int c = n%100/10;
			int d = n%10;

			cout << digits[b] << " tram ";

			if(c + d != 0) {
				if(c == 0)
					cout << "le ";
				else if(c == 1) 
					cout << "muoi ";
				else
					cout << digits[c] << " muoi ";

				if(d == 5) cout << "lam";
				else if (d != 0)
					cout << digits[d];
			}

		} else if ( n >= 10) {
			int c = n/10;
			int d = n%10;
			if(c == 1) 
				cout << "muoi ";
			else
				cout << digits[c] << " muoi ";

			if(d == 5) cout << "lam";
			else if (d != 0)
				cout << digits[d];

		} else {
			cout << digits[n];
		}
		cout << endl;
	}

	return 0;
}