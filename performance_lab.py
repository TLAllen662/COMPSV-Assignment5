from collections import Counter

# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    # Refactor note: I optimized this version by using Counter, which keeps the same
    # hash-based counting strategy but reduces Python-level bookkeeping compared to
    # repeatedly calling dict.get() in a manual loop.
    counts = Counter(numbers)
    return max(counts, key=counts.get)

"""
Original vs. Refactored Comparison for problem 1:
- Original version: two explicit passes (count values, then scan counts). Time: O(n + k), Space: O(k).
- Refactored version: one counting pass + max lookup over the hash map. Time: O(n + k), Space: O(k).
- Performance: Both have the same asymptotic complexity, but Counter reduces manual dictionary operations and is more efficient in Python because the counting logic is handled in optimized C-backed code paths.
- Space usage: No meaningful asymptotic change; still O(k) for distinct values. The trade-off is that the hash map is kept in memory to avoid repeated scans.
- Could it be optimized further? Only by using different data structures or constraints (for example, if values were already sorted, a linear scan could work, but that changes the input assumptions).
- Trade-off: This version is cleaner and slightly more efficient in practice, while still using extra memory for the frequency map instead of a nested-loop approach.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    unique_items = []

    for value in nums:
        if value not in seen:
            seen.add(value)
            unique_items.append(value)

    return unique_items

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) because we still scan the whole list to determine whether each value is new.
- Worst-case: O(n) because each element is checked once and possibly inserted into the seen set.
- Average-case: O(n) as set membership and addition are O(1) on average.
- Space complexity: O(k), where k is the number of distinct values kept in the result and the set.
- Why this approach? The set allows O(1)-average membership checks, while the output list preserves the original encounter order.
- Could it be optimized? Not significantly for a single pass; we must keep some memory of previously seen values to preserve uniqueness without reordering.
- Trade-offs: We use extra memory for the set, which makes the algorithm much faster than repeatedly scanning the output list, but it increases space usage compared with an in-place approach.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for value in nums:
        complement = target - value
        if complement in seen:
            pair = tuple(sorted((value, complement)))
            pairs.add(pair)
        seen.add(value)

    return sorted(pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) because we can finish the scan if the target is not found only after checking each value once.
- Worst-case: O(n) because each element is processed once and set membership is O(1) on average.
- Average-case: O(n) with hashing for the seen set.
- Space complexity: O(n) in the worst case, because the set of seen values can grow to include all elements and the result set stores up to O(n) unique pairs.
- Why this approach? A hash set allows efficient lookup of complements, turning the pair search into a linear pass rather than a nested loop.
- Could it be optimized? A two-pointer solution is O(n log n) after sorting, but the hash-based method is usually faster for unsorted data and preserves the unique-pair requirement.
- Trade-offs: The hash-set method is fast and simple, but it uses extra memory and may need conversion to sorted tuples/pairs to keep results deterministic.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n, initial_capacity=4):
    if n < 0:
        raise ValueError("n must be non-negative")
    if initial_capacity <= 0:
        raise ValueError("initial_capacity must be positive")

    values = []
    capacity = initial_capacity

    print(f"Initial capacity: {capacity}")

    for item in range(1, n + 1):
        if len(values) == capacity:
            new_capacity = capacity * 2
            print(f"Resizing: {capacity} -> {new_capacity}")
            values = values.copy()
            capacity = new_capacity

        values.append(item)
        print(f"Added {item}; current size: {len(values)}; capacity: {capacity}")

    return values

"""
Time and Space Analysis for problem 4:
- When do resizes happen? A resize occurs whenever the current number of stored elements reaches the current capacity, so the list doubles at sizes 4, 8, 16, 32, ... for an initial capacity of 4.
- What is the worst-case for a single append? O(capacity) during a resize, because every existing element must be copied into the new array.
- What is the amortized time per append overall? O(1) amortized, because expensive resize operations happen infrequently while many appends are cheap.
- Space complexity: O(n) for the final list, with temporary extra space during a resize of up to O(capacity) while the new array is built.
- Why does doubling reduce the cost overall? Each resize copies a large array, but each element participates in only a constant number of re-copying events as capacity doubles repeatedly, so total copying cost stays proportional to the total number of inserts.
- Trade-offs: Doubling reduces the number of resize operations but temporarily uses extra memory during growth; this is the classic trade-off between occasional large copy costs and many cheap append operations.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    running_sum = 0

    for value in nums:
        running_sum += value
        totals.append(running_sum)

    return totals

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) because the function must process each item at least once to build the cumulative sums.
- Worst-case: O(n) because the loop runs across the full list.
- Average-case: O(n) for the same reason.
- Space complexity: O(n) to store the result list of running totals.
- Why this approach? We maintain a single running sum and append to a new list, which keeps the algorithm simple and avoids re-summing earlier elements.
- Could it be optimized? Not in asymptotic terms for producing all cumulative totals; every output value must be calculated once.
- Trade-offs: This method is efficient and easy to read, but it creates a second array for the results, which costs memory in exchange for avoiding redundant recomputation.
"""


def run_tests():
    # Problem 1 tests
    assert most_frequent([]) is None
    assert most_frequent([42]) == 42
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([5, 5, 1, 1]) in {5, 1}
    assert most_frequent([2, 2, 3, 3, 3]) == 3

    # Problem 2 tests
    assert remove_duplicates([]) == []
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([8, 2, 8, 3, 2, 4]) == [8, 2, 3, 4]
    assert remove_duplicates([7]) == [7]

    # Problem 3 tests
    assert find_pairs([], 5) == []
    assert find_pairs([1, 2, 3, 4], 5) == [(1, 4), (2, 3)]
    assert find_pairs([10, 20, 30, 40], 50) == [(10, 40), (20, 30)]
    assert find_pairs([1, 2, 3], 10) == []
    assert find_pairs([5, 6, 7, 8, 9], 13) == [(5, 8), (6, 7)]

    # Problem 4 tests
    import io
    from contextlib import redirect_stdout

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        result = add_n_items(6, initial_capacity=4)
    output = buffer.getvalue()
    assert result == [1, 2, 3, 4, 5, 6]
    assert "Initial capacity: 4" in output
    assert "Resizing: 4 -> 8" in output
    assert "Added 6" in output

    empty_buffer = io.StringIO()
    with redirect_stdout(empty_buffer):
        empty_result = add_n_items(0, initial_capacity=4)
    assert empty_result == []
    assert "Initial capacity: 4" in empty_buffer.getvalue()

    # Problem 5 tests
    assert running_total([]) == []
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([5, -2, 3]) == [5, 3, 6]
    assert running_total([0, 0, 0]) == [0, 0, 0]
    assert running_total([-1, -2, 3, -4]) == [-1, -3, 0, -4]

    print("All performance_lab tests passed.")


if __name__ == "__main__":
    run_tests()
