class Solution:
    def findContentChildren(self, student: List[int], cookie: List[int]) -> int:
        n = len(student)
        m = len(cookie)

        # Sort both arrays
        student.sort()
        cookie.sort()

        studentIndex = 0
        cookieIndex = 0

        # Try to assign cookies until any one list is fully processed
        while studentIndex < len(student) and cookieIndex < len(cookie):
            # If the cookie satisfies the student's greed
            if cookie[cookieIndex] >= student[studentIndex]:
                studentIndex += 1
            # Move to next cookie in both cases
            cookieIndex += 1

        # Number of students satisfied is equal to studentIndex
        return studentIndex