#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;
const int N = 2e5;

ull n, p, r, l, res;
int test;
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("5.in", "r", stdin);
	freopen("5.out", "w", stdout);
	#endif

	cin >> test;
	while (test--) {
		res = 0;
		cin >> n >> p >> l >> r;

		if(l == 1 && r == n)
		{
			cout << 0 << endl;
			continue;
		}

		if(r == p || l == p) {
			if(p == l) {
				if (l != 1)
					res += 1;
				if (r != n)
					res += r - l + 1;
			} else { // p == r
				if (r != n)
					res += 1;
				if (l != 1)
					res += r - l + 1;
			}
		}
		else if (l < p && p < r) {
			if (p - l < r - p) {
				if (l != 1) {
					res += p - l + 1;
					if (r != n)
						res += r - l + 1;
				} else { // l == 1 && r != n
					res = r - p + 1;
				}
			} else {
				if (r != n) {
					res += r - p + 1;
					if (l != 1)
						res += r - l + 1;
				} else { // r == n && l != 1
					res = p - l + 1;
				}
			}
		} else if ( p < l) {
			res = l - p + 1;
			if (r != n)
				res += r - l + 1;
		} else {
			res = p - r + 1;
			if (l != 1)
				res += r - l + 1;
		}

		cout << res << endl;
	}
	
	return 0;
}