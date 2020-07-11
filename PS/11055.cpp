#include <bits/stdc++.h>
using namespace std;

int a[1001] = {0};

// maximum sum
int dp[1001] = {0};

int main()
{
    int n, ret = 0;
    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
        int maxsum= 0;
        for (int j = 0; j < i; ++j) {
            if (a[i] > a[j])
                maxsum = max(maxsum, dp[j]);
        }
        dp[i] = maxsum + a[i];
        ret = max(dp[i], ret);
    }
    printf("%d\n", ret);
}

/* dp[i] = max(sum of LIS)
 * time = O(N^2), memory = O(N)
 */