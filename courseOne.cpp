#include <iostream>
#include <vector>
using namespace std;

class Solution{
	vector<vector<int> >adjs;
	vector<bool> marcados;
	vector<bool> is_on_stack;
	int n;

	bool dfs(int u){
		marcados[u] = true;
		is_on_stack[u] = true;
		for(int v : adjs[u]){
			if(!marcados[v]){
				if(!dfs(v)){
					return false;
				}
			}
			else{
				if(is_on_stack[v]){
					return false;
				}
			}
		}
		//tira ele da pilha aqui pq n achou ciclo e ta retornando a call stack
		is_on_stack[u] = false;
		return true;

	}
	
	public:
		bool canFinish(int num_courses, vector<vector<int> >& prereq){
			n = num_courses;
			adjs = vector<vector<int> >(n);
			marcados = vector<bool> (n);
			is_on_stack = vector<bool> (n);


			int arestas = prereq.size();

			for(int i = 0; i++; i< arestas){
				int u = prereq[i][1];
				int v = prereq[i][0];
				adjs[u].push_back(v);	
			}

			for(int i = 0; i < n; i++){
				if(!marcados[i]){
					if(!dfs(i)){
						return false;
					}
				}
				return true;
			}
		}
	};





int main(){
	int numCourses = 5;
	
		



}
