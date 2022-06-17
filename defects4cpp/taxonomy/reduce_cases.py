import glob
import sys
import json

proj_name = sys.argv[1]
start_proj = sys.argv[2]
end_proj = sys.argv[3]

# Opening JSON file
with open("./defects4cpp/taxonomy/" + proj_name + "/meta.json", "r+") as meta_data_file:

    # returns JSON object as
    # a dictionary
    data = json.load(meta_data_file)

    # Iterating through the json
    # list


    # Closing file
    meta_data_file.close()

    file_path_list = glob("./targets/openssl/buggy#**/AUTOMAKE_TEST_CASE.output")

    d4cpp_list = range(start_proj, end_proj)

    failing_index = 0
    num_cases = 0
    cnt_to_reduce = 0
    num_to_reduce = []

    remove_tests = ['test_ssl_new', 'test_fuzz']

    for proj in d4cpp_list:
        test_list = "./targets/openssl/buggy#__/AUTOMAKE_TEST_CASE.output".replace("__", str(proj))
        with test_list as f:
            lines = f.readlines()

        lines = [line.rstrip('\n') for line in lines]

        print(lines)
        defects_list = data["defects"]
        num_cases = defects_list[proj]["num_cases"]
        failing_index = defects_list[proj]["case"]

        for idx, test in enumerate(lines):
            for rm_test in remove_tests:
                if rm_test in test:
                    num_cases = num_cases - 1
                    num_to_reduce.append(test)

        for rm_num in num_to_reduce:
            if rm_num < failing_index:
                cnt_to_reduce = cnt_to_reduce + 1
            else:
                break

        failing_index = failing_index - cnt_to_reduce

        defects_list[proj]["num_cases"] = num_cases
        defects_list[proj]["case"] = failing_index

        meta_data_file.seek(0)
        json.dump(data, meta_data_file, indent=4)


