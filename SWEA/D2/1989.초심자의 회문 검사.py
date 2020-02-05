# D2 초심자의 회문 검사
def palindrome(word):
    word_list = list(word)
    for j in range(len(word_list)):
        if word_list[j] != word_list[len(word_list)-j-1]:
            return 0
    return 1
T = int(input())
for i in range(T):
    word = input()
    print("#{0} {1}".format(i+1,palindrome(word)))