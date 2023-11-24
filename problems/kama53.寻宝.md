

如果你的图相对较小且比较密集，而且你更注重简单性和空间效率，数组实现可能更合适。

如果你的图规模较大，尤其是在稀疏图中，而且你更注重时间效率和通用性，优先级队列实现可能更合适。

其关键 在于弄清楚  minDist 的定义

```CPP

#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// 定义图的邻接矩阵表示
const int INF = INT_MAX; // 表示无穷大
typedef vector<vector<int>> Graph;

// 使用Prim算法找到最小生成树
void primMST(const Graph& graph, int startVertex) {
    int V = graph.size();

    // 存储顶点是否在最小生成树中
    vector<bool> inMST(V, false);

    // 存储最小生成树的边权重
    vector<int> key(V, INF);

    // 优先队列，存储边权重和目标顶点
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    // 初始顶点的权重设为0，加入优先队列
    key[startVertex] = 0;
    pq.push({0, startVertex});

    while (!pq.empty()) {
        // 从优先队列中取出权重最小的边
        int u = pq.top().second;
        pq.pop();

        // 将顶点u标记为在最小生成树中
        inMST[u] = true;

        // 遍历u的所有邻居
        for (int v = 0; v < V; ++v) {
            // 如果v未在最小生成树中，且u到v的权重小于v的当前权重
            if (!inMST[v] && graph[u][v] < key[v]) {
                // 更新v的权重为u到v的权重
                key[v] = graph[u][v];
                // 将(u, v)添加到最小生成树
                pq.push({key[v], v});
            }
        }
    }

    // 输出最小生成树的边
    cout << "Edges in the Minimum Spanning Tree:\n";
    for (int i = 1; i < V; ++i) {
        cout << i << " - " << key[i] << " - " << i << "\n";
    }
}

int main() {
    // 例子：无向图的邻接矩阵表示
    Graph graph = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    // 从顶点0开始运行Prim算法
    primMST(graph, 0);

    return 0;
}
```


```CPP 
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// 定义图的邻接矩阵表示
const int INF = INT_MAX; // 表示无穷大
typedef vector<vector<int>> Graph;

// 使用Prim算法找到最小生成树
void primMST(const Graph& graph, int startVertex) {
    int V = graph.size();

    // 存储顶点是否在最小生成树中
    vector<bool> inMST(V, false);

    // 存储每个顶点的权重
    vector<int> key(V, INF);

    // 初始化起始顶点的权重为0
    key[startVertex] = 0;

    // 存储最小生成树的边权重
    vector<int> parent(V, -1);

    // 构建最小生成树
    for (int count = 0; count < V - 1; ++count) {
        // 从未在最小生成树中的顶点中找到权重最小的顶点
        int u = -1;
        for (int v = 0; v < V; ++v) {
            if (!inMST[v] && (u == -1 || key[v] < key[u])) {
                u = v;
            }
        }

        // 将顶点u标记为在最小生成树中
        inMST[u] = true;

        // 更新u的邻居的权重和父节点
        for (int v = 0; v < V; ++v) {
            if (graph[u][v] != 0 && !inMST[v] && graph[u][v] < key[v]) {
                key[v] = graph[u][v];
                parent[v] = u;
            }
        }
    }

    // 输出最小生成树的边
    cout << "Edges in the Minimum Spanning Tree:\n";
    for (int i = 1; i < V; ++i) {
        cout << parent[i] << " - " << key[i] << " - " << i << "\n";
    }
}

int main() {
    // 例子：无向图的邻接矩阵表示
    Graph graph = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    // 从顶点0开始运行Prim算法
    primMST(graph, 0);

    return 0;
}
```
