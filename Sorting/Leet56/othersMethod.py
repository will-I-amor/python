class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return []
        else:
            newl = []
            #intervals.sort()
            #sort isn't going to work
            intervals.sort(key = lambda x: x.start)
            #this is the part that I don't quite understand
            print intervals
            for interval in intervals:
                if not newl:
                    newl.append([interval.start,interval.end])
                elif newl[-1][1]>=interval.start:
                    newl[-1][0] = min(newl[-1][0],interval.start)
                    newl[-1][1] = max(newl[-1][1],interval.end)
                else:
                    newl.append([interval.start,interval.end])
            return newl
