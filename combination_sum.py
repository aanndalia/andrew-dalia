def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    if not candidates:
        return []

    all_combos = set()
    memo_set = set()

    def recurse(candidates, target, cur_combo, cur_combo_sum):
        memo_key = tuple(sorted(cur_combo))
        if cur_combo_sum == target:
            all_combos.add(memo_key)
            return

        if cur_combo_sum > target:
            return

        if memo_key in memo_set:
            return

        for i, num in enumerate(candidates):
            recurse(candidates, target, cur_combo + [num], cur_combo_sum + num)

        memo_set.add(tuple(sorted(cur_combo)))
        return

    recurse(candidates, target, [], 0)
    return list(all_combos)