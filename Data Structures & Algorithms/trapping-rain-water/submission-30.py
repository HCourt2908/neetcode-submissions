class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0        
        i = 0

        while i < len(height):
            lBoundary = height[i]
            lowers = []
            j = i+1

            if j == len(height):
                break

            while (height[j]<lBoundary):
                lowers.append(height[j])
                j += 1
                if j >= len(height):
                    break   

            if not (j == len(height)):
                rBoundary = height[j]
                lowerBoundary = min(lBoundary, rBoundary)
                for x in lowers:
                    print(f"added {lowerBoundary-x} water")
                    water += (lowerBoundary-x)
                i = j
            else:
                endWater = True
                for x in range(len(lowers)-1):
                    if lowers[x] > height[j-1]:
                        endWater = False
                    #elif lowers[x] == height[j-1]:
                        #for y in range(x):
                            #water += (height[j-1]-lowers[y])
                print(endWater)
                if endWater == True:
                    for x in lowers:
                        water += (height[j-1]-x)
                    i = len(height)
                else:
                    i += 1
                
        return water
            
            #send out a j to find where to fill in from
            # then use i to fill in
