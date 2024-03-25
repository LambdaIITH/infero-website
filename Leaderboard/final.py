import json
import os
import sys

# current codes_num = [473618 6 480016 6 485152 6 499604 6 506063 6]
# prefer giving all contest_ids instead of only giving 1

contest_ids = [sys.argv[i] for i in range(1, len(sys.argv)) if i % 2 != 0]
#

num_questions = [sys.argv[i] for i in range(2, len(sys.argv)) if i % 2 == 0]

points = [
    [str(i*500) for i in range(1, int(num_questions[j])+1)] for j in range(len(num_questions))
]

contests_num = len(contest_ids)

def main():

    scores = dict()  # for each handle, store and add the score

    # getting all users and scores
    participants = set()
    for idx, contest in enumerate(contest_ids):
        print(f'Contest: {contest}')
        os.system(f'python3 acpl.py {contest} "output"{
                  idx + 1}.json {" ".join(points[idx])}')
        # print(f'python3 acpl.py {contest} output{idx + 1}.json {" ".join(points[idx])}')
        print('Done')
        print('------------------')
        print('------------------')
        print('------------------')

        with open(f"output{idx + 1}.json", 'r') as file:
            data = json.load(file)
            for participant in data:
                handle = participant['handle']
                participants.add(handle)

    print(participants)
    scores = {participant: {f"contest_{
        i+1}": 0 for i in range(contests_num)} for participant in participants}
    for idx, contest in enumerate(contest_ids):
        with open(f"output{idx + 1}.json", 'r') as file:
            data = json.load(file)
            for participant in data:
                handle = participant['handle']
                score = participant['score']
                scores[handle][f"contest_{idx+1}"] = score

                # if 'total' not in scores[handle]:
                # scores[handle]['total'] = 0
                # else:

        os.remove(f"output{idx + 1}.json")

    for idx, participant in enumerate(participants):
        sorted_scores = []
        tot = 0
        for i in range(contests_num):
            sorted_scores.append(scores[participant][f"contest_{i+1}"])
        sorted_scores.sort(reverse=True)
        for i in range(contests_num):
            print(sorted_scores[i])
        print("hi")
        for i in range(contests_num):
            tot += sorted_scores[i]
            if i == contests_num-3 and i > 2:
                break
        print(tot)
        scores[participant]['total'] = tot

    # sorting the scores
    scores = sorted(scores.items(), key=lambda x: x[1]['total'], reverse=True)

    # convert back to dict
    scores = {handle[0]: handle[1] for handle in scores}

    # assigning ranks
    for idx, handle in enumerate(scores):
        scores[handle]['rank'] = idx + 1

    # just assuring it gets rendered properly
    scores = [{"handle": key, **values} for key, values in scores.items()]

    final_dict = {"users": scores}

    with open('final.json', 'w') as file:
        json.dump(final_dict, file, indent=4)


if __name__ == "__main__":
    main()
