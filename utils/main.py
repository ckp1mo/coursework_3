from utils.utils import load_operation_json, get_5_executed_operations, sort_date
from utils.output_result import print_result

operations = 'operations.json'


# данные файла json
operations_load = load_operation_json(operations)

# список отсортированных дат в обратном порядке(на убывание)
sorted_date = sort_date(operations_load)

# список последних пяти исполненных операций
last_5_ex_operations = get_5_executed_operations(operations_load, sorted_date)

# печать последних операций в удобном формате
print_result(last_5_ex_operations)
