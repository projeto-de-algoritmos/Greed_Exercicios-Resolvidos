class Solution:
    def ordenacao_diferenca(self, pair):
        return abs(pair[0] - pair[1])
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=self.ordenacao_diferenca)

        n1 = len(costs) / 2
        n2 = len(costs) / 2

        count = 0
        for item in reversed(costs):
            if(item[0] < item[1]):
              if(n1 == 0):
                count = count + item[1]
              else:
                count = count + item[0]
                n1 = n1 - 1
            else:
              if(n2 == 0):
                count = count + item[0]
              else:
                count = count + item[1]
                n2 = n2 - 1
                
        return count