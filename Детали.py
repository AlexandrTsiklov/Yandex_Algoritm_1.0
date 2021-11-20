N, K, M = map(int, input().split())
big_weigh, average_weigh, small_weigh = N, K, M


# def average_small(average__weigh, small__weigh):
#     local_count = 0
#     while average__weigh >= small__weigh:
#         average__weigh -= small__weigh
#         local_count += 1
#     return average__weigh, local_count
#
#
# common_count = 0
# while big_weigh >= average_weigh:
#     big_weigh -= average_weigh
#     remain, result = average_small(average_weigh, small_weigh)
#     big_weigh += remain
#     common_count += result
#
# print(common_count)

count_average, count_small = 0, 0
while (big_weigh >= average_weigh) and (average_weigh >= small_weigh):
    count_average = big_weigh // average_weigh
    big_weigh %= average_weigh

    count_small += (average_weigh // small_weigh) * count_average
    big_weigh += (average_weigh % small_weigh) * count_average

print(count_small)
