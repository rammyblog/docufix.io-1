# def do_something(chunk):
#     pass

import pandas as pd

# def readSas(filename, chunk):
#     # with open(filename, 'r') as reader:
#     rdr = pd.read_sas(filename, chunk=100000)
#     for chunk in rdr:
#         print(chunk)



# # def get_txt_word(filename):
# #     # base_dir = settings.BASE_DIR
# #     # dataform = os.path.join(base_dir, filename[1:])
# #     with open(filename, 'r') as reader:
# #         word = ''
# #         for line in reader.readlines():
# #             
# #         return word 



def readSas(filename):
    rdr = pd.read_sas(filename)
    word = ''
    for chunk in rdr:
        word+=chunk
    return word
