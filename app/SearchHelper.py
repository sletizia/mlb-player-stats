import csv
import os
import Levenshtein


class SearchHelper():

    def __init__(self):
        # Load the player list from csv when object is created
        self.player_list = []
        with open('app/master.csv', 'r', encoding="Latin1") as csvfile:
            readCSV = csv.reader(csvfile)
            for row in readCSV:
                # print(row)
                # print(row[0])
                self.player_list.append(row[1])

    def get_matches(self, search_name):
        # Use Levenshtein distance to find closest matches to the searched name
        matches = [[100, ""], [100, ""], [100, ""]]

        for name in self.player_list:
            # use a priority queue maybe? check that code from the class
            # get the lev score
            score = Levenshtein.distance(search_name, name)
            for i in matches:
                if score < i[0]:
                    i[0] = score
                    i[1] = name
                    break

        print(matches)
        return(matches)



        



if __name__ == "__main__":
    # ob = SearchHelper()
    # ob.get_matches("randal arazorana")

    print(os.listdir())