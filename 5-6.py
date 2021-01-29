with open('file_6.txt', encoding='utf8') as file:
    subj_list = [line.replace('(', ' ').replace(':', ' ').split() for line in file]
    subj_dict = {el[0]: el[1:] for el in subj_list}
    for key, value in subj_dict.items():
        subj_dict[key] = sum([int(el) for el in value if el.isdigit()])
    print(subj_dict)
