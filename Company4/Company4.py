"""
We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user2 = ["a", "/one", "/two"]
user3 = ["/red", "/orange", "/yellow", "/green", "/blue", "/purple", "/white", "/amber", "/HotRodPink", "/BritishRacingGreen"]
user4 = ["/red", "/orange", "/amber", "/random", "/green", "/blue", "/purple", "/white", "/lavender", "/HotRodPink", "/BritishRacingGreen"]
user5 = ["a"]

Sample output:

findContiguousHistory(user0, user1)
   /pink
   /register
   /orange

findContiguousHistory(user1, user2)
   (empty)

findContiguousHistory(user2, user0)
   a

findContiguousHistory(user5, user2)
   a

findContiguousHistory(user3, user4)
   /green
   /blue
   /purple
   /white

findContiguousHistory(user4, user3)
   /green
   /blue
   /purple
   /white

n: length of the first user's browsing history
m: length of the second user's browsing history

"""

user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user2 = ["a", "/one", "/two"]
user3 = ["/red", "/orange", "/yellow", "/green", "/blue", "/purple", "/white", "/amber", "/HotRodPink",
         "/BritishRacingGreen"]
user4 = ["/red", "/orange", "/amber", "/random", "/green", "/blue", "/purple", "/white", "/lavender", "/HotRodPink",
         "/BritishRacingGreen"]
user5 = ["a"]


def calculateClicksByDomain(counts):
    total_hits = {}
    for count in counts:
        hits, domain = count.split(",")
        parsed_domain = domain.split(".")
        for i, domain_part in enumerate(parsed_domain):
            total_hits[".".join(parsed_domain[i:])] = total_hits.get(".".join(parsed_domain[i:]), 0) + int(hits)
    print(total_hits)
    return total_hits


def findContiguousHistory(userA, userB):
    if not userA or not userB:
        return []
    if userA and userB:
        if userA[0] == userB[0]:
            return [userA[0]] + findContiguousHistory(userA[1:], userB[1:])
        else:
            return max(findContiguousHistory(userA, userB[1:]), findContiguousHistory(userA[1:], userB), key=len)


contiguous_list = []


# findContiguousHistory(user0, user1, contiguous_list)

# print(contiguous_list)

def findContiguousHistory2(userA, userB):
    length, max_x, max_y = 0, 0, 0
    space_matrix = [[0 for _ in range(len(userA) + 1)] for _2 in range(len(userB) + 1)]
    for i in range(1, len(userA)):
        for j in range(1, len(userB)):
            if userA[i] == userB[j]:
                space_matrix[i][j] = space_matrix[i - 1][j - 1] + 1
                if space_matrix[i][j] > max_x:
                    max_x, max_y = i, j
                    length = space_matrix[i][j]
            else:
                space_matrix[i - 1][j - 1] = max(space_matrix[i][j - 1], space_matrix[i - 1][j])
    print(userB[j-length:j])


findContiguousHistory(user0, user1)
