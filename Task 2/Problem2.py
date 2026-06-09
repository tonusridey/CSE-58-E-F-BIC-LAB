def frequent_words(text, k):
    count = {}

    for i in range(len(text) - k + 1):
        k_mer = text[i:i+k]
        if k_mer in count:
            count[k_mer] += 1
        else:
            count[k_mer] = 1

    max_count = max(count.values())

    result = []
    for k_mer in count:
        if count[k_mer] == max_count:
            result.append(k_mer)

    return result
