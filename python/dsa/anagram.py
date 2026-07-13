s ="anagram"
t="nagaram"


def is_anagram(s, t):
    hashmap1 ={}
    hashmap2 = {}
    for char in s:
        if char in hashmap1:
            hashmap1[char] +=1
        else:
            hashmap1[char] =1
    for char in t:
        if char in hashmap2:
            hashmap2[char] +=1
        else:
            hashmap2[char] =1

def is_anagram(s, t):
    hashmap1 = {}
    hashmap2 = {}
    for char in s:
        if char in hashmap1:
            hashmap1[char] += 1
        else: 
            hashmap1[char] = 1
    for char in t:
        if char in hashmap2:
            hashmap2[char] += 1
        else: 
            hashmap2[char] = 1
    
    return hashmap1 == hashmap2
    
print(is_anagram(s, t))







# for word in s: 
#     if word in hashmap1:
#         hashmap1[word] += 1
#     else:
#         hashmap1[word] = 1

# for word in t:
#     if word in hashmap2:
#         hashmap2[word] += 1
#     else:
#         hashmap2[word] = 1

# print(hashmap1)
# print(hashmap2)
