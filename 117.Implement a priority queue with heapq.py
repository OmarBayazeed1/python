#117.Implement a priority queue with heapq
import heapq as h
data=[]
print('data',data)
h.heappush(data,10)
print('data',data)

h.heappush(data,5)
print('data',data)

h.heappush(data,2)
print('data',data)

h.heappush(data,1)

print(data)
print(type(data))
smallest=h.heappop(data)
print(smallest)
print(data)


