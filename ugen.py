import random
import names
import typer

department = ['Legal', 'Defence', 'Development', 'Sales', 'Marketing', 'HR', 'Engineering']

middle_names = [True, False]


def my_gen(input_file):
    employee_count = random.randint(0, 10)
    for i in range(employee_count):
        employee_id = random.randint(1000, 9999)
        employee_first = names.get_first_name()
        employee_middle = random.choice(middle_names)
        if employee_middle:
            employee_middle = names.get_first_name()
        else:
            employee_middle = ''
        employee_last = names.get_last_name()
        employee_dep = random.choice(department)
        input_file.write(f'{str(employee_id)}:{employee_first}:{employee_middle}:{employee_last}:{employee_dep}\n')


input1 = open("input_file1.txt", "w", encoding='utf-8')
input2 = open("input_file2.txt", "w", encoding='utf-8')
input3 = open("input_file3.txt", "w", encoding='utf-8')

my_gen(input1)
my_gen(input2)
my_gen(input3)

input1.close()
input2.close()
input3.close()

# OUTPUT


def my_output(input_file):
    for x in input_file.readlines():
        emp_split = x.split(':')
        user_name = emp_split[1][:1].lower() + emp_split[2][:1].lower() + emp_split[3].lower()
        output1.write(f'{emp_split[0]}:{user_name}:{emp_split[1]}:{emp_split[2]}:{emp_split[3]}:{emp_split[4]}')


input1 = open('input_file1.txt', 'r', encoding='utf-8')
input2 = open('input_file2.txt', 'r', encoding='utf-8')
input3 = open('input_file3.txt', 'r', encoding='utf-8')
output1 = open('output_file.txt', 'w', encoding='utf-8')

my_output(input1)
my_output(input2)
my_output(input3)

input1.close()
input2.close()
input3.close()
output1.close()


app = typer.Typer()


@app.command()
def my_help():
    print('python3 ugen.py –h')


if __name__ == '__main__':
    app()