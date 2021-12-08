def count_num(num):
    with open("d:\\code\\learning python\\input.txt", "r+") as f:
        lines = []
        for line in f:
            tokens = line.split(',')
            lines.append(tokens)

        n = 0
        for i in lines:
            if num == int(i[0]):
                n += 1
            elif num == int(i[1]):
                n += 1
        return n


def sum_num():
    with open("d:\\code\\learning python\\input.txt", "r+") as f:
        lines = []
        for line in f:
            tokens = line.split(',')
            lines.append(tokens)
            sum_tokens = int(tokens[0]) + int(tokens[1])
            print("sum: " + str(sum_tokens) + " | ", line, end='')


def sum_num_write():
    with open("d:\\code\\learning python\\input.txt", "r+") as f:
        lines = []
        sum_lst = []
        for line in f:
            tokens = line.split(',')
            lines.append(tokens)
            sum_tokens = int(tokens[0]) + int(tokens[1])

            sum_tokens_str = "sum: " + str(sum_tokens) + " | " + line
            sum_lst.append(sum_tokens_str)

        with open("d:\\code\\learning python\\input.txt", "r+") as f:
            for i in sum_lst:
                f.write(i)


# print(count_num(6))
# sum_num()
sum_num_write()