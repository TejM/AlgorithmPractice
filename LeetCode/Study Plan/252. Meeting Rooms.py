class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda time: time[0])
        
        for x in range(len(intervals)-1):
            if intervals[x+1][0] < intervals[x][1]:
                return False
        return True
