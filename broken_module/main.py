import re
import sys
import traceback


def force_load(name_of_module):
    # someth = compile(module, name_of_module, 'exec')

    name_of_module += '.py'

    with open(name_of_module) as file:
        lines = [line for line in file]

        module_without_errors = False

        ldict = {}

        while not module_without_errors:
            try:
                module_without_errors = True
                exec(''.join(lines), globals(), ldict)

            except EOFError as eof:
                module_without_errors = True

            except Exception as ex:
                trback = traceback.format_exc()
                matches = re.findall(r'"<string>", line \d+', trback)

                #try:
                number = re.findall(r'\d+', matches[0])
                line_numb = int(number[0])
                # except Exception as ex:
                #    ex.args.__setattr__('matches', matches)

                module_without_errors = False

                lines.pop(line_numb-1)

        # print(ldict)
        return ldict


# print(force_load('module'))