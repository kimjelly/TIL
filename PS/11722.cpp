#include <bits/stdc++.h>
using namespace std;

int dp[1001] = {0};

int main()
{
    int n, len = 0, val;
    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        scanf("%d", &val);

        if (len == 0 || dp[len - 1] > val) {
            dp[len++] = val;
        } else {
            auto lb = lower_bound(dp, dp + len, val, greater<int>());
            *lb = val;
        }
    }
    printf("%d\n", len);
}

/* dp[i] = max(len of LDS)
 * time = O(N lg N), memory = O(N)
 * upper_bound 쓰려고 하면 index 처리가 더 힘들어진다. lower bound의 방향을 바꾸는 게 맞는듯
 */