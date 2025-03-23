#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        // Use a vector of vectors for adjacency list
        vector<vector<pair<int, int>>> adj(n);
        
        for (auto& it : roads) {
            adj[it[0]].push_back({it[1], it[2]});
            adj[it[1]].push_back({it[0], it[2]});
        }

        // Priority queue (Min Heap) -> {distance, node}
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

        // Distance array and ways array initialization
        vector<long long> dist(n, LLONG_MAX), ways(n, 0);
        dist[0] = 0;
        ways[0] = 1;
        pq.push({0, 0});

        // Modulo value
        int mod = (int)(1e9 + 7);

        while (!pq.empty()) {
            auto [dis, node] = pq.top();
            pq.pop();

            for (auto& [adjNode, edW] : adj[node]) {
                long long newDist = dis + edW; // Use long long to prevent overflow

                // If a shorter path is found, update distance & ways
                if (newDist < dist[adjNode]) {
                    dist[adjNode] = newDist;
                    pq.push({newDist, adjNode});
                    ways[adjNode] = ways[node];
                }
                // If another shortest path is found, add to ways count
                else if (newDist == dist[adjNode]) {
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod;
                }
            }
        }

        return ways[n - 1] % mod;
    }
};
