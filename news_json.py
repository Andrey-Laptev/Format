import json

def get_sorted_words_list(file):
    with open(file, "rt", encoding="UTF-8") as f:
        obj = json.load(f)
    words = []
    for item in obj["rss"]["channel"]["items"]:
        for elem in item["description"].lower().split(" "):
            words.append(elem)
    words.sort()
    return words

def print_top_length_words(sorted_list):
    buf = sorted_list[0]
    counts = {buf: 0}
    for wrd in sorted_list:
        if wrd == buf:
            counts[wrd] += 1
        else:
            counts[wrd] = 1
            buf = wrd

    words_set_sorted = list(set(sorted_list))
    words_set_sorted.sort(key=len)
    words_set_sorted.reverse()

    result = []
    for wrd in words_set_sorted:
        if len(wrd) < 7:
            break
        for elem in result:
            if counts[wrd] > elem[1]:
                result.insert(result.index(elem), [wrd, counts[wrd]])
                if len(result) > 10:
                    result = result[:-1]
                break
        else:
            if len(result) < 10:
                result.append([wrd, counts[wrd]])

    print("Топ самых длинных слов длиннее 6 символов:")
    for elem in result:
        print(f"{result.index(elem) + 1}. '{elem[0]}' - {elem[1]} шт.")

def main():
    print_top_length_words(get_sorted_words_list("newsafr.json"))

if __name__ == "__main__":
    main()