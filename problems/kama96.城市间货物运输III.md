
# 96. 城市间货物运输 III 

[题目链接](https://kamacoder.com/problempage.php?pid=1154) 

【题目描述】

某国为促进城市间经济交流，决定对货物运输提供补贴。共有 n 个编号为 1 到 n 的城市，通过道路网络连接，网络中的道路仅允许从某个城市单向通行到另一个城市，不能反向通行。

网络中的道路都有各自的运输成本和政府补贴，道路的权值计算方式为：运输成本 - 政府补贴。

权值为正表示扣除了政府补贴后运输货物仍需支付的费用；

权值为负则表示政府的补贴超过了支出的运输成本，实际表现为运输过程中还能赚取一定的收益。

请计算在最多经过 k 个城市的条件下，从城市 src 到城市 dst 的最低运输成本。

【输入描述】

第一行包含两个正整数，第一个正整数 n 表示该国一共有 n 个城市，第二个整数 m 表示这些城市中共有 m 条道路。

接下来为 m 行，每行包括三个整数，s、t 和 v，表示 s 号城市运输货物到达 t 号城市，道路权值为 v。

最后一行包含三个正整数，src、dst、和 k，src 和 dst 为城市编号，从 src 到 dst 经过的城市数量限制。

【输出描述】

输出一个整数，表示从城市 src 到城市 dst 的最低运输成本，如果无法在给定经过城市数量限制下找到从 src 到 dst 的路径，则输出 "unreachable"，表示不存在符合条件的运输方案。

输入示例：

```
6 7
1 2 1
2 4 -3
2 5 2
1 3 5
3 5 1
4 6 4
5 6 -2
2 6 1
```

输出示例：

```
0
```

## 思路 

本题为单源有限最短路问题，同样是 [kama94.城市间货物运输I](./kama94.城市间货物运输I.md) 延伸题目。

在 [kama94.城市间货物运输I](./kama94.城市间货物运输I.md) 中我们讲了：**对所有边松弛一次，相当于计算 起点到达 与起点一条边相连的节点 的最短距离**。 

节点数量为n，那么起点到终点，最多是 n-1 条边相连。 那么对所有边松弛 n-1 次 就一定能得到 起点到达 终点的最短距离。 

（如果对以上讲解看不懂，建议详看 [kama94.城市间货物运输I](./kama94.城市间货物运输I.md) ） 

本题是最多经过 k 个城市， 那么是 k + 1条边相连的节点。 这里可能有录友想不懂为什么是k + 1，来看这个图： 

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20240402115614.png) 

图中，节点2 最多已经经过2个节点 到达节点4，那么中间是有多少条边呢，是 3 条边对吧。 

所以本题就是求，起点最多经过k + 1 条边到达终点的最短距离。 


对所有边松弛一次，相当于计算 起点到达 与起点一条边相连的节点 的最短距离，那么对所有边松弛 k + 1次，就是求 起点到达 与起点k + 1条边相连的节点的 最短距离。 

如果 终点数值没有被计算覆盖，那就是无法到达。 

**注意**： 本题是  [kama94.城市间货物运输I](./kama94.城市间货物运输I.md) 的拓展题，如果对 bellman_ford 没有深入了解，强烈建议先看 [kama94.城市间货物运输I](./kama94.城市间货物运输I.md) 再做本题。   

理解以上内容，其实本题代码就很容易了，bellman_ford 标准写法是松弛 n-1 次，本题就松弛 k + 1次就好。

如果大家理解后，建议先自己写写代码，提交一下看看，因为 这里还有一个坑，如果不自己去试试，体会就不够深刻了。 



代码如下： （关键地方详细注释）

```CPP
#include <iostream>
#include <vector>
#include <list>
#include <climits>
using namespace std;

int main() {
    int src, dst,k ,p1, p2, val ,m , n;
    
    cin >> n >> m;

    vector<vector<int>> grid;

    for(int i = 0; i < m; i++){
        cin >> p1 >> p2 >> val;
        // p1 指向 p2，权值为 val
        grid.push_back({p1, p2, val});
    }

    cin >> src >> dst >> k;

    vector<int> minDist(n + 1 , INT_MAX);
    minDist[src] = 0;
    vector<int> minDist_copy(n + 1); // 用来记录每一次遍历的结果
    for (int i = 1; i <= k + 1; i++) {
        minDist_copy = minDist; // 获取上一次计算的结果
        for (vector<int> &side : grid) {
            int from = side[0];
            int to = side[1];
            int price = side[2];
            //cout << f[0] << " " << f[1] << " " << f[2] << endl;
            if (minDist_copy[from] != INT_MAX && minDist[to] > minDist_copy[from] + price) minDist[to] = minDist_copy[from] + price;
        }

    }

    if (minDist[dst] == INT_MAX) cout << "unreachable" << endl; // 不能到达终点
    else cout << minDist[dst] << endl; // 到达终点最短路径

}

```
