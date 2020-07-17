

def process_results(in_file):
    modules_dict = {}
    with open(in_file, 'r') as f:
        for l in f:
            if l[7:17] == 'NA       =':
                module = l[18:24]
            if l[9:13] == 'MCUE':
                location = '&'.join(l[20:40].split())
                if module:
                    if module in modules_dict.keys():
                        if location != modules_dict[module]:
                            print('Module with two locatios:', module)
                            return 0
                        else:
                            continue
                    modules_dict[module] = location
                    module = None
    with open('modules_locations', 'w') as f:
        [f.write(k + ' ' + v + '\n') for k, v in modules_dict.items()]

    print('Total modules:', len(modules_dict))


if __name__=='__main__':
    in_file = 'results_all_modules'
    process_results(in_file)
