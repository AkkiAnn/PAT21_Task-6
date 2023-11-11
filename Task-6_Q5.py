def distribute_mangoes(mangoes, students):
    if students == 0:
        return 0
    if students >= len(mangoes):
        return min(mangoes)
    mangoes.sort() 
    min_difference = float('inf')
    for i in range(len(mangoes) - students + 1):
        max_mangoes = mangoes[i + students - 1]
        min_mangoes = mangoes[i]
        difference = max_mangoes - min_mangoes
        if difference < min_difference:
            min_difference = difference
    return min_difference
mangoes = [10, 20, 30, 40, 50, 60, 70]
students = 3
result = distribute_mangoes(mangoes, students)
print("Minimum difference between bags:", result)
