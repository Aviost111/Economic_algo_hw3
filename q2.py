import copy


def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    """Implements the weighted round-robin algorithm for fair item allocation.

        Different rights and different valuations
        >>> weighted_round_robin([1, 2, 3], [[17, 10, 8], [10, 7, 9], [10, 10, 7]], 0.1)
        player 2 takes item 0 with value of 10
        player 1 takes item 2 with value of 9
        player 2 takes item 1 with value of 10

        same rights and same valuations
        >>> weighted_round_robin([1, 1, 1], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0.5)
        player 0 takes item 0 with value of 1
        player 1 takes item 1 with value of 1
        player 2 takes item 2 with value of 1

        same rights and different valuations
        >>> weighted_round_robin([1, 1, 1], [[1, 2, 3], [3, 8, 1], [2, 1, 3]], 0.5)
        player 0 takes item 2 with value of 3
        player 1 takes item 1 with value of 8
        player 2 takes item 0 with value of 2

        dictator
        >>> weighted_round_robin([1,2,1000],[[1000,1000,1000],[1000,1000,1000],[1,1,1]],0.2)
        player 2 takes item 0 with value of 1
        player 2 takes item 1 with value of 1
        player 2 takes item 2 with value of 1

        >>> weighted_round_robin([1,9,6],[[1,1,1],[1,1,1],[1,1,1]],0.6)
        player 1 takes item 0 with value of 1
        player 2 takes item 1 with value of 1
        player 1 takes item 2 with value of 1

        """
    val_copy = copy.deepcopy(valuations)
    # holds amount of items per person
    people = []
    # holds each persons value
    people_amount = []
    person = 0
    # holds what item hasn't been taken
    items = []
    # fill items
    for i in range(len(valuations[0])):
        items.append(i)
        # fill values and put 1 item for each person so you won't divide by 0 if y=0(even though in the course it says to start with 0)
    for r in rights:
        people.append(((r / 1 + y), person))
        people_amount.append(1)
        person += 1
        # while items left
    while len(valuations[0]) > 0:
        # sort by value to get the highest value
        sorted_people = sorted(people, key=lambda x: x[0], reverse=True)
        # winner
        cur_person = sorted_people.pop(0)
        # winners list
        cur_person_list = valuations[cur_person[1]]
        # winners fav item
        max_item = max(cur_person_list)
        # winners fav item index to discard for everyone
        max_item_index = cur_person_list.index(max_item)
        count = 0
        orig_max_item_index = -1
        # finds the original location of the item for prints
        for j in val_copy[cur_person[1]]:
            # if he already took the item move on(for items with the same valuations)
            if j == max_item and count in items:
                orig_max_item_index = count
                items.remove(count)
                break
            count += 1
        # add 1 to owned items
        people_amount[cur_person[1]] += 1
        print(f"player {cur_person[1]} takes item {orig_max_item_index} with value of {max_item}")
        # remove item from everywhere
        for j in valuations:
            j.pop(max_item_index)
        people = sorted_people
        # update winners score
        people.append((rights[cur_person[1]] / (people_amount[cur_person[1]] + y), cur_person[1]))


if __name__ == "__main__":
    import doctest

#     doctest.testmod()
    weighted_round_robin([1, 9, 6], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0.2)
