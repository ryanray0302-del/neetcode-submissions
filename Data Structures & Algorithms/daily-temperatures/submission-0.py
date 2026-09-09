class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        day = []
        result = [0] * len(temperatures )

        for i in range(len(temperatures)):
          

          while day and temperatures[i] > temperatures[day[-1]]: 
            old_day = day.pop()
            difference = i - old_day
            result[old_day] = difference

          day.append(i)
          
        return result 