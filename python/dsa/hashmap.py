# nums = [1,2,3,1]

# def contains_duplicate(nums):
#     seen = {} # আমাদের মেমরি বা ডিকশনারি

#     for num in nums:
#         # যদি সংখ্যাটি আমাদের ডিকশনারিতে আগেই থাকে, তারমানে এটা ডুপ্লিকেট!
#         if num in seen: 
#             return True
#         # যদি না থাকে, তবে ডিকশনারিতে এন্ট্রি করে রাখো যে একে একবার দেখা গেছে
#         seen[num] = True
#     return False # পুরো লুপ শেষ হওয়ার পরও ডুপ্লিকেট না মিললে False

text ="apple banana apple cherry banana apple"
text = text.split()

def check_duplicate_words(text):
    seen = {}
    for word in text:
        if word in seen:
            seen[word] +=1
        else: 
            seen[word] = 1
    return seen
print(check_duplicate_words(text))