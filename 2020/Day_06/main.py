
with open("input.txt", 'r') as file:
    content = file.read()

content = content.strip()
content = content.replace('\n', ' ')
t_groups = content.split('  ')
groups = []

for t_group in t_groups:
    group = t_group.split(' ')
    groups.append(group)

# Part One
group_yes_count = []

for group in groups:
    questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for person in group:
        for answer in person:
            if answer in questions:
                questions.remove(answer)
    group_yes_count.append(26 - len(questions))

if len(groups) != len(group_yes_count):
    print('groups and answers do not match')

print(f'Part One: {sum(group_yes_count)}')

# Part Two
group_yes_count = []

for group in groups:
    questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for answer in questions.copy():
        is_yes = True

        for person in group:
            if answer not in person:
                is_yes = False

        if not is_yes:
            questions.remove(answer)

    group_yes_count.append(len(questions))


if len(groups) != len(group_yes_count):
    print('groups and answers do not match')

print(f'Part Two: {sum(group_yes_count)}')
