from typing import List

class Solution:
    def ordenacao_diferenca(self, pair):
        return abs(pair[0] - pair[1])
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=self.ordenacao_diferenca)

        a = len(costs) / 2
        b = len(costs) / 2

        total_cost = 0
        for cost_a, cost_b in reversed(costs):
            if(cost_a < cost_b):
              if(a > 0):
                total_cost += cost_a
                a = a - 1
              else:
                total_cost += cost_b
                
            else:
              if(b > 0):
                total_cost += cost_b
                b = b - 1
              else:
                total_cost += cost_a

        return total_cost