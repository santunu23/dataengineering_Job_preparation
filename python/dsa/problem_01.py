# প্রশ্ন: তোমাকে একটি অ্যারে দেওয়া আছে nums = [2, 7, 11, 15] এবং একটি টার্গেট ভ্যালু target = 9। 
# তোমাকে অ্যারের এমন দুটি সংখ্যার ইনডেক্স খুঁজে বের করতে হবে, যাদের যোগফল হবে ৯।


# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
        

def two_sum_optimized(nums, target): 
    seen={}
    for i, num in enumerate(nums):
        remaining= target - num
        if remaining in seen:
            return [seen[remaining],i]
        seen[num]=i


print(two_sum_optimized([2, 7, 11, 15], 9))        
