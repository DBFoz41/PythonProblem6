"""
File reading class

methonds include: process and return the number of candidates,
a dict of candidates, a list of votes, number of votes
"""

class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_obj = None
        self.number_of_candidates = 0
        self.dict_of_candidates = {}
        self.str_num_cand = ""
        self.list_str_vote = []
        self.list_vote = [[0,0,0]]


    def file_open(self):
        self.file_obj = open(self.file_name, "r")

    def file_read_get_num_candidates(self):
        self.str_num_cand = self.file_obj.readline()
        self.number_of_candidates = int(self.str_num_cand[0])
        return self.number_of_candidates

    def file_read_get_dict_of_candidates(self):
        for x in range(self.number_of_candidates):
            name_string = self.file_obj.readline()
            name_split = name_string.split("\n")
            self.dict_of_candidates[x+1] = name_split[0]
        return self.dict_of_candidates

    def file_read_get_list_of_votes(self):
        self.list_str_vote = self.file_obj.readlines()
        self.list_vote = [[0,0,0] for i in range(len(self.list_str_vote))]

        for index, i in enumerate(self.list_str_vote):
            self.list_vote[index][0] = int(i[0])
            self.list_vote[index][1] = int(i[2])
            self.list_vote[index][2] = int(i[4])
        return self.list_vote

        

    def file_close(self):
        self.file_obj.close()