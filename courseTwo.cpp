#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution{
	vector<vector<int>> adjs;
	vector<bool> mk;
	vector<bool> is_on_stack;
	vector<int> postOrder;
	int n;
	bool ciclico;

	void dfs(int u){
		mk[u] = true;
		is_on_stack[u] = true;
		for(int v : adjs[u]){
			if(ciclico){
				return;
			}

			if(!mk[v]){
				dfs[v];
			}

			else{
				if(is_on_stack[v]){
					ciclico = true;
					return;
				}
			}
		}
		postOrder.push_back(u);
		is_on_stack[u] = false;




	}

	public:
		vector<int> findOrder(int numCourses, vector<vector<int>>& prereq){
			n = numCourses;
			ciclico = false;
			adjs = vector<vector<int>> (n);
			mk = vector<bool> (n);
			is_on_stack = vector<bool> (n);

			int arestas = prereq.size();
			for(int i =0; i<arestas; i++){
				//prereq 1 é prereq de 0		
				int u = prereq[i][1];
				int v = prereq[i][0];
				adjs.push_back(v);

			}
			
			for(int i = 0; i < n; i++){
				if(!mk[i]){
					dfs(i);
				}
			

			}

			if(ciclico){
				return {};
			}

			vector<int> post_order_reversed(postOrder);
			reverse(post_order_reversed.begin(), post_order_reversed.end());

			return post_order_reversed;
		}
	
	




	

};



int main(){

	int num = 5;
	vector<vector<int>> prerequisitos {{1,0},{3,1},{2,3},{2,4},{4,1}};
	Solution obj;
	vector<int> resposta = obj.findOrder(num, prerequisitos);

	for(int x : resposta){
		cout << x;
	}

	return 0;
}
