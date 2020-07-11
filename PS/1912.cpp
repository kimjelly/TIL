#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    scanf("%d", &n);

    int m = -987654321, val, ans = -987654321;
    for (int i = 0; i < n; ++i) {
        scanf("%d", &val);
        m = max(m + val, val);
        ans = max(ans, m);
    }
    printf("%d\n", ans);
}

/* max(dp[i-1] + a[i], a[i])를 비교
 * time = O(N), memory = O(1)
 */