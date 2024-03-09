def solution(park, routes):
    result = []

    s_h = 0
    s_w = 0
    standard_width = len(park[0])
    standard_height = len(park)
    for i in range(0, standard_height):
        for k in range(0, standard_width):
            if park[i][k] == "S":
                s_h = i
                s_w = k
                break

    for route in routes:
        route_split = route.split(" ")
        direction = route_split[0]
        count = int(route_split[1])

        if direction == "E":
            if s_w + count < standard_width:
                is_hurdle = False
                for i in range(s_w, count):
                    if park[s_h][i] == "X":
                        is_hurdle = True
                        break
                if not is_hurdle:
                    s_w += count
        elif direction == "W":
            if s_w - count >= 0:
                is_hurdle = False
                for i in range(count, -1, -1):
                    if i < 0 or park[s_h][i] == "X":
                        is_hurdle = True
                        break
                if not is_hurdle:
                    s_w -= count
        elif direction == "S":
            if s_h + count < standard_height:
                is_hurdle = False
                for i in range(s_h, count):
                    if park[i][s_w] == "X":
                        is_hurdle = True
                        break
                if not is_hurdle:
                    s_h += count
        else:
            if s_h - count >= 0:
                is_hurdle = False
                for i in range(count, -1, -1):
                    if i < 0 or park[i][s_w] == "X":
                        is_hurdle = True
                        break
                if not is_hurdle:
                    s_h -= count

    result.append(s_h)
    result.append(s_w)

    return result


def solution2(park, routes):
    result = []

    s_h = 0
    s_w = 0
    standard_width = len(park[0])
    standard_height = len(park)
    op = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for i in range(0, standard_height):
        for k in range(0, standard_width):
            if park[i][k] == "S":
                s_h = i
                s_w = k
                break

    for route in routes:
        route_split = route.split(" ")
        direction = route_split[0]
        count = int(route_split[1])
        cur_h = s_h
        cur_w = s_w

        for i in range(count):
            h = s_h + op[direction][0]
            w = s_w + op[direction][1]

            if 0 <= h <= standard_height - 1 and 0 <= w <= standard_width - 1 and (park[h][w] != "X"):
                s_h = h
                s_w = w
            else:
                s_h = cur_h
                s_w = cur_w
                break

    result.append(s_h)
    result.append(s_w)

    return result


if __name__ == "__main__":
    park = ["OOO", "OSO", "OXO", "OOO"]
    routes = ["W 2", "N 1"]
    result1 = solution(park, routes)  # 일부 통과
    result2 = solution2(park, routes)  # 전체 통과
