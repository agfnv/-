# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common_participants = participants1.intersection(participants2)
    return sorted(common_participants)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники: {result}")
# TODO Провеьте работу функции с разделителем отличным от запятой
