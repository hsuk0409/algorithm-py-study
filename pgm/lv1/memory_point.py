def solution(name, yearning, photo):
    answer = []
    name_index = 0
    name_point_map = {}
    for n in name:
        name_point_map[n] = yearning[name_index]
        name_index += 1

    for p in photo:
        point = 0
        for name in p:
            find_point_or_null = name_point_map.get(name)
            if find_point_or_null:
                point += find_point_or_null
        answer.append(point)

    return answer


if __name__ == "__main__":
    solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
             [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
