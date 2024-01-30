class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        # Sort the people list in descending order of height (i) and ascending order of index (j)
        people.sort(key=lambda x: (-x[0], x[1]))

        # Iterate through each person in the sorted list
        for p in people:
            # p[1] corresponds to the second element of the sublist, which is the person's position in the queue. p[1] is used to determine the position at which to insert the person p into the queue.
            queue.insert(p[1], p)

        # Return the reconstructed queue
        return queue
