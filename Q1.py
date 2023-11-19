class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        s_points=sorted(points)
        s=s_points[0][0]
        e=s_points[0][1]
        cnt=1
        idx=1
        while idx<n:
            if s_points[idx][0]<=e:
                s=s_points[idx]
                e=min(s_points[idx][1],e)
            else:
                cnt+=1
                s=s_points[idx][0]
                e=s_points[idx][1]
            idx+=1
        return cnt
        