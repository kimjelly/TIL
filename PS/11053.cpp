#include <bits/stdc++.h>
using namespace std;

int a[1001] = {0};
int dp[1001] = {0};

int main()
{
    int n, ret = 0;
    scanf("%d", &n);

    /*
    int dp[1001] = {0};
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &a[i]);
        
        int maxlen = 0;
        for (int j = 1; j < i; ++j) {
            if (a[j] < a[i])
                maxlen = max(dp[j], maxlen);
        }
        dp[i] = maxlen + 1;
        ret = max(dp[i], ret);
    }
    printf("%d\n", ret);
    */

    int val, len = 0; // a[i]를 쓸 필요가 없음
    for (int i = 0; i < n; ++i) {
        scanf("%d", &val);
        if (len == 0 || dp[len - 1] < val) {
            dp[len++] = val;
        } else {
            auto lb = lower_bound(dp, dp + len, val);
            *lb = val;
        }
    }
    printf("%d\n", len);
}

/* 1) 길이 중심
 * dp[i] = i번째 원소를 마지막으로 하는 LIS의 길이
 *         (k in [1, i-1], a[k] < a[i] => max(dp[k]) + 1)
 * time = O(N^2), memory = O(N)
 * 
 * 2) LIS 중심 
 * dp[i] = 길이 i인 LIS를 만들 수 있는 마지막 원소 중 가장 작은 값
 * len(dp)가 곧 현재까지 만들 수 있는 LIS의 길이
 * initial list = empty
 *  - (dp == empty) || dp[last] < a[i]
 *     => dp[++last] = a[i]
 *     현재 LIS의 마지막 원소보다 a[i]가 더 크니 길이가 더 긴 LIS를 만들 수 있음
 *  - not
 *     => dp 안에서 a[i]의 lower_bound를 찾아서 치환
 * 핵심은 dp list가 계속 정렬된 상태를 유지하는 것
 *   => lower_bound가 계속 log(N)을 유지
 * time = O(N lg N), memory = O(N)
 */