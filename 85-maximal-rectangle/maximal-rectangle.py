class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, width * height)
            stack.append(i)
        
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxi=-1e9
        arr=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0:
                    arr[j]=int(matrix[i][j])
                elif matrix[i][j]=="1":
                    arr[j]+=1
                else:
                    arr[j]=0
            maxi=max(maxi,self.largestRectangleArea(arr))
        return maxi