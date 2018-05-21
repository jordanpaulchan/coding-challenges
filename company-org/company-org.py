def company_org(employees):
    managers_map = {}
    for employee in employees:
        if employee[1] not in managers_map:
            managers_map[employee[1]] = []

        if employee[0] not in managers_map:
            managers_map[employee[0]] = []

        managers_map[employee[1]].append(employee)

    if not managers_map[None]:
        print('No CEO')
        return None

    dash_set = {managers_map[None][0][0]: ''}
    stack = [managers_map[None][0]]

    while stack:
        current = stack.pop()
        print('{}{} ({}) {}'.format(
            dash_set[current[0]], current[0], current[2], current[3]))

        for reportee in managers_map[current[0]]:
            dash_set[reportee[0]] = dash_set[reportee[1]] + '-'
            stack.append(reportee)


employees = [
    ['Karl', 'Nancy', 'Manager', 2009],
    ['Adam', 'Karl', 'Technician', 2010],
    ['Bob', 'Karl', 'Technician', 2012],
    ['Cathy', 'Wendy', 'Manager', 2013],
    ['Nancy', None, 'CEO', 2007],
    ['Wendy', 'Nancy', 'Technician', 2012],
    ['John', 'Adam', 'Woker', 2014]
]

company_org(employees)
