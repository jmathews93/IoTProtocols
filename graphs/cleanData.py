##
## RUN WITH PYTHON3
##
import csv, sys, os


def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        path_to_write = sys.argv[2]
        print(path_to_write)
        base = os.path.basename(file_name)
        # file_no_ext = os.path.splitext(base)[0]
        file_to_save_to = os.path.splitext(base)[0] + '.csv'
        clean_list = []

        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        for i in range(len(data) - 1):
            if data[i][1] != '0':
                # print(data[i])
                clean_list.append(data[i])

        # print(clean_list)

        with open(path_to_write + file_to_save_to + file_to_save_to, 'w') as write_file:
            wr = csv.writer(write_file, dialect='excel')
            wr.writerows(clean_list)
        # print(data)
        print(path_to_write + file_to_save_to)


if __name__ == "__main__":
    main()
