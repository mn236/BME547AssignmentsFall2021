import logging


def fibinaci(input_list):
    next_entry = input_list[-2] + input_list[-1]
    input_list.append(next_entry)
    logging.warning("This iteration is {}".format(input_list))  # Used to log warnings
    if next_entry <= 100:
        fibinaci(input_list)
    else:
        logging.warning("This is the last iteration")


if __name__ == '__main__':
    logging.basicConfig(filename="example.log", filemode="w",
                        level=logging.INFO)
    start_list = [0, 1]
    fibinaci(start_list)