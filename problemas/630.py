from typing import List
import heapq 


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        sorted_courses = sorted(courses, key=lambda x: x[1])
        
        max_heap, tempo_total, count = [], 0, 0
        for duracao, termino in sorted_courses:
            heapq.heappush(max_heap,-duracao)
            tempo_total += duracao
            count += 1
            if tempo_total > termino: 
                tempo_total += heapq.heappop(max_heap)
                count -= 1
        
        return count