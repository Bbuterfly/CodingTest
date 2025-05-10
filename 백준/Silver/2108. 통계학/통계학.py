import sys
from collections import Counter

# N : N개의 정수, 1<=N<=5*10^5
def main():
    input = sys.stdin.readline
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    
    avg = round(sum(nums)/N)
    
    nums.sort()
    median = nums[N//2]
    
    count = Counter(nums)
    freq = count.most_common()
    max_freq = freq[0][1]
    
    modes = [num for num, cnt in freq if cnt == max_freq]
    modes.sort()
    mode = modes[0] if len(modes) == 1 else modes[1]
    
    ran = max(nums) - min(nums)
    
    print(f"{avg}\n{median}\n{mode}\n{ran}")

if __name__ == "__main__":
    main()