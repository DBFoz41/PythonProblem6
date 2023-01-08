"""
The Australian Voting Problem

Determine an election winner with a ranked voting system
"""

import file_reader as fr




class VotingCount:

    def __init__(self):
        self.votes = []
        self.number_of_votes = 0
        self.vote_tally = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
        self.percent_of_vote = {1:0.0, 2:0.0, 3:0.0, 4:0.0, 5:0.0, 6:0.0, 7:0.0, 8:0.0, 9:0.0, 10:0.0}
        self.max_votes = 0
        self.lowest_vote = []
        self.candidates_to_eliminate = []
        self.dict_of_candidate_names = {}
        
    def tablulate_votes(self, list_of_votes):
        self.votes = list_of_votes
        self.number_of_votes = len(self.votes)
        
        for i in self.votes:
            match i[0]:
                case 1:
                    self.vote_tally[1] = self.vote_tally[1]+1
                
                case 2:
                    self.vote_tally[2] = self.vote_tally[2]+1

                case 3:
                    self.vote_tally[3] = self.vote_tally[3]+1

                case 4:
                    self.vote_tally[4] = self.vote_tally[4]+1
                
                case 5:
                    self.vote_tally[5] = self.vote_tally[5]+1

                case 6:
                    self.vote_tally[6] = self.vote_tally[6]+1

                case 7:
                    self.vote_tally[7] = self.vote_tally[7]+1

                case 8:
                    self.vote_tally[8] = self.vote_tally[8]+1
                
                case 9:
                    self.vote_tally[9] = self.vote_tally[9]+1

                case 10:
                    self.vote_tally[10] = self.vote_tally[10]+1
        

        for index, votes in enumerate(self.vote_tally.values()):
            self.percent_of_vote[index+1] = votes/self.number_of_votes
            if self.percent_of_vote[index+1] == 0:
                self.percent_of_vote.pop(index+1)

        return self.percent_of_vote  

    def remove_eliminated_votes(self, candidates_to_remove):
        for i in candidates_to_remove:
            for j in self.votes:
                if j[0] == i:
                    j = j.pop(0)
        return self.votes

    def check_for_winner(self):
        self.max_votes = max(self.percent_of_vote.values())
        self.max_candidate = max(self.percent_of_vote, key=self.percent_of_vote.get)

        if self.max_votes > 0.5:
            self.candidates_to_eliminate = []
        else:
            self.lowest_vote = sorted(self.percent_of_vote,reverse=True)
            i = 0
            while self.percent_of_vote[self.lowest_vote[i]] < self.percent_of_vote[self.lowest_vote[i+1]]:
                self.candidates_to_eliminate.append(self.lowest_vote[i])
                i += 1
        return self.candidates_to_eliminate

    def print_winner(self, dict_of_candidate_names):
        self.dict_of_candidate_names = dict_of_candidate_names
        print("winner")
        print(self.dict_of_candidate_names[self.max_candidate])
        
        
        
def execute_main():
    list_of_votes = []
    file = fr.FileReader("inputFile.txt")
    file.file_open()
    num_of_candidates = file.file_read_get_num_candidates()
    dict_of_candidates = file.file_read_get_dict_of_candidates()
    list_of_votes = file.file_read_get_list_of_votes()
    file.file_close()
    list_of_candidates_to_eliminate = [0]


    print(num_of_candidates)
    print(dict_of_candidates)
    print(list_of_votes)

    vote = VotingCount()

    while list_of_candidates_to_eliminate != []:
        vote2 = vote.tablulate_votes(list_of_votes)
        list_of_candidates_to_eliminate = vote.check_for_winner()
        if list_of_candidates_to_eliminate != []:
            list_of_votes = vote.remove_eliminated_votes(list_of_candidates_to_eliminate)
        else:
            continue
    vote.print_winner(dict_of_candidates)

if __name__ == "__main__":
    execute_main()