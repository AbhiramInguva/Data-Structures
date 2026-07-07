# Linked List Interview Roadmap — 1 Week (Python)

**Goal:** Go from theory-only to solving any linked list question on LeetCode.
**Target:** TCS, EY, PwC campus drives + general product-based rounds.

---

## Ground Rules for Every Problem
1. Draw the list as boxes and arrows on paper first.
2. Simulate pointer moves by hand before typing code.
3. Write pointer reassignments as separate lines first — only compress into one-liners once it works.
4. Use this debug helper locally:
```python
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
```
5. Standard node class (LeetCode gives you this already):
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Day 1 — Build It Yourself + Dummy Node
- Write a singly linked list class from scratch: insert at head/tail/position, delete a node, traverse/print, find length. No references — just do it.
- Concept: dummy node technique
```python
dummy = ListNode(0)
dummy.next = head
```
- **Problems:**
  - 707 — Design Linked List
  - 206 — Reverse Linked List (iterative)
  - 203 — Remove Linked List Elements

## Day 2 — Two-Pointer Fundamentals
- Concept: slow-fast (tortoise-hare) pointer technique
- **Problems:**
  - 876 — Middle of the Linked List
  - 141 — Linked List Cycle
  - 142 — Linked List Cycle II (find cycle start)

## Day 3 — Merging + Removal Patterns
- Concept: merge technique, dummy + two pointers combined
- **Problems:**
  - 21 — Merge Two Sorted Lists
  - 83 — Remove Duplicates from Sorted List
  - 19 — Remove Nth Node From End of List

## Day 4 — Reversal Variants + Palindrome
- Concept: reversing a sublist, combining slow-fast + reversal
- **Problems:**
  - 92 — Reverse Linked List II
  - 234 — Palindrome Linked List
  - 160 — Intersection of Two Linked Lists

## Day 5 — Arithmetic & Restructuring
- Concept: simulating number addition, splitting/interleaving a list
- **Problems:**
  - 2 — Add Two Numbers
  - 24 — Swap Nodes in Pairs
  - 143 — Reorder List

## Day 6 — Advanced Grouping & Sorting
- Concept: reverse in fixed-size chunks, merge sort applied to a linked list
- **Problems:**
  - 25 — Reverse Nodes in k-Group
  - 148 — Sort List
  - 23 — Merge k Sorted Lists

## Day 7 — Hard Structural + Mock Round
- Concept: cloning with extra pointers, doubly linked list design
- **Problems:**
  - 138 — Copy List with Random Pointer
  - 146 — LRU Cache (doubly linked list + hashmap — very common design question)
- **Mock round:** pick 4 random problems from Days 1–6, solve back to back, no notes, timed.

---

## Quick Reference — Concept → Problems Map
| Concept | Problems |
|---|---|
| Basic traversal/dummy node | 707, 203, 21, 83 |
| Slow-fast pointer | 876, 141, 142, 234, 143 |
| Reversal (iterative/recursive) | 206, 92, 25 |
| Merging | 21, 148, 23 |
| Arithmetic simulation | 2 |
| Structural manipulation | 19, 24, 143 |
| Hashing/cloning | 160, 138 |
| Design | 707, 146 |

**Non-negotiable minimum (if a day gets tight):** 206, 876, 21, 141, 19, 142, 234, 2, 143, 25, 138, 146 — these cover ~90% of what TCS/EY/PwC-style rounds ask.

**If you truly run out of time:** cut Day 6 (25, 148, 23) last — these are the "separates you from others" tier, not core-interview-essential for the companies you listed.
