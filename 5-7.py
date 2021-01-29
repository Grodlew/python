import json
with open('file_7.txt', encoding='utf-8') as file:
    content = [[int(i) if i.isdigit() else i for i in line.split()] for line in file]
    profit = [el[2] - el[3] for el in content]
    # не смог сделать словарь из двух списков (фирмы и их прибыль), поэтому сначала соединил их:
    for el in range(len(content)):
        content[el].append(profit[el])
    cl_profit = [el for el in profit if el >= 0]  # список с прибылями(без убытков) для подсчета средней прибыли
    avg_profit = round(sum(cl_profit) / len(cl_profit), 2)
    final_list = [{el[0]: el[4] for el in content}, {'average_profit': avg_profit}]

with open('file_7.json', 'w') as file:
    json.dump(final_list, file)
