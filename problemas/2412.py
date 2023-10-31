from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        t_boas = [t for t in transactions if t[0] <= t[1]]
        t_ruins = [t for t in transactions if t[0] > t[1]]
        
        t_ruins.sort(key=lambda t: t[1])
        
        qtd_min, total_gasto = 0, 0
        
        for cost, cashback in t_ruins:
            total_gasto += cost
            qtd_min = max(qtd_min, total_gasto)
            total_gasto -= cashback
        
        if t_boas:
            melhor_t = max(t_boas, key=lambda t: t[0])
            total_gasto += melhor_t[0]
            qtd_min = max(qtd_min, total_gasto)
        
        return qtd_min