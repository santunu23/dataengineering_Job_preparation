# প্রশ্ন: তোমাকে একটি সোর্টেড অ্যারে দেওয়া আছে numbers = [2, 3, 4, 7, 11, 15] এবং target = 9। 
# তোমাকে এমন দুটি সংখ্যা খুঁজে বের করতে হবে যাদের যোগফল ৯। (শর্ত: তুমি কোনো এক্সট্রা মেমরি বা 
# ডিকশনারি ব্যবহার করতে পারবে না, অর্থাৎ Space Complexity হতে হবে $O(1)$)।

def two_sum_sorted(numbers, target):
    # দুটি পয়েন্টার সেট করা
    left = 0
    right = len(numbers) - 1

    while left < right: 
        current_sum = numbers[left] + numbers[right]
        # ১. যদি পারফেক্ট ম্যাচ পেয়ে যাই
        if current_sum == target:
            return [left, right]
        # ২. যোগফল ছোট হলে বামের পয়েন্টার ডানে সরাও (ভ্যালু বাড়ানোর জন্য) 
        elif current_sum < target:
            left += 1
        else:
            right -= 1