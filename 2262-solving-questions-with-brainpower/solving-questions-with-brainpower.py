from functools import lru_cache

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @lru_cache(None)  # Memoization
        def solve(i):
            if i >= n:
                return 0
            
            # Option 1: Solve the question
            points, brainpower = questions[i]
            solve_question = points + solve(i + brainpower + 1)
            
            # Option 2: Skip the question
            skip_question = solve(i + 1)
            
            return max(solve_question, skip_question)
        
        return solve(0)
