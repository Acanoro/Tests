def vote(votes):
    votes_unique = list(set(votes))
    common_meaning = 0
    number_repetitions = 0

    for vu in votes_unique:
        if number_repetitions < votes.count(vu):
            common_meaning = vu
            number_repetitions = votes.count(vu)

    return common_meaning


if __name__ == '__main__':
    print(vote([1, 2, 3, 4, 5]))
    print(vote([1, 2, 3, 2, 2]))
