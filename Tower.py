
'''Вычисление минимального количества шагов для перепоса башни с стержня на стержень.'''
'''disks - диски'''
'''rods_list - Список с стержнями'''
'''start_rod - стержень с которого берется диск'''
'''end_nod - стержень куда кладется диск'''
'''mem_nod - промежуточный стержень'''
'''count - счетчик шагов'''
def hanoi_tower(disks: int, rods_list : list, start_rod : list, end_rod : list, mem_rod : list, default_rod_list : list, start_rod_index : int, end_rod_index :int, count : list):

    if disks == 0:
        return

    if len(rods_list) == 3:
        hanoi_tower(disks - 1, rods_list, start_rod, mem_rod, end_rod, default_rod_list, default_rod_list.index(start_rod), default_rod_list.index(mem_rod), count)

        move_disk(disks, start_rod, end_rod, default_rod_list.index(start_rod), default_rod_list.index(end_rod), count)

        hanoi_tower(disks - 1, rods_list, mem_rod, end_rod, start_rod, default_rod_list, default_rod_list.index(mem_rod), default_rod_list.index(end_rod), count)
    else:
        hanoi_tower(disks - 1, rods_list[:-1], start_rod, rods_list[-1], end_rod, default_rod_list, default_rod_list.index(start_rod), default_rod_list.index(rods_list[-1]), count)

        move_disk(disks, start_rod, end_rod, default_rod_list.index(start_rod), default_rod_list.index(end_rod), count)

        hanoi_tower(disks - 1, rods_list[:-1], rods_list[-1], end_rod, start_rod, default_rod_list, default_rod_list.index(rods_list[-1]), default_rod_list.index(end_rod), count)

'''Перемещение диска'''
'''disk - диск который нужно переместить'''
'''from_rod - с какого стержня'''
'''to_rod - на какой стержнь'''
'''count - счетчик шагов'''
def move_disk(disk : int, from_rod : list, to_rod : list, from_rod_index : int, to_rod_index : int, count: list):
    to_rod.append(from_rod.pop())
    row = f"Блин {disk}: Стержень {str(from_rod_index)} -> Стержень {str(to_rod_index)}"
    print(row)
    count.append(disk)
    save_row_to_file(row)

'''Инициализация списка с стержнями'''
'''disks - количество дисков'''
'''rods - количество стержней'''
def init_rods(disks : int, rods : int):
    rods_dictionary = [[]]

    for i in range(1, rods + 1):
        rods_dictionary.append([])

    for j in range(1, disks + 1):
        rods_dictionary[1].append(j)

    return  rods_dictionary

'''Сохранение в файл'''
'''row - строка которую нужно записать в файл'''
'''file - название файла'''
def save_row_to_file(row : str = "", file="решение.txt"):
    with open(file, "a") as f:
        f.write(f"{row}\n")


def main():
    rods = input("Введите количество стержней: ")
    disks = input("Введите количество дисков: ")
    count = []

    if rods.isnumeric() and disks.isnumeric():
        if int(disks) <= 0:
            print("Количество дисков не может быть меньше 1")
            return

        if int(rods) <= 2:
            print("Количество стержней не может быть меньше 3")
            return 0

        rods_list = init_rods(int(disks), int(rods))

        if int(disks) == 1:
            print(f"Блин 1: Стержень 1 -> Стержень 2")
        else:
            hanoi_tower(int(disks), rods_list, rods_list[1], rods_list[-1], rods_list[2], rods_list, rods_list.index(rods_list[1]), rods_list.index(rods_list[-1]), count)
            print(f"Всего шагов: {len(count)}")
    else:
        print("Введены неккоректные данные.")

main()