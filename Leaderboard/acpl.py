import datetime
import random
import hashlib
import requests
import string
import time
from pprint import pprint
from dotenv import load_dotenv
import os
import json
import sys
load_dotenv()


def get_final_standings(score_distribution, api_key, api_secret, contest_id, group_code='NpnwJNnkjM'):
    """
    Returns final standings in the form of a list of lists
    Each list contains the handle name and the score of the participant
    Returned list is sorted in descending order of score
    """

    # Calculate per minute penalty and the minimum points for each problem
    minPoints = [int(0.3 * score) for score in score_distribution]
    per_minute_penalty = [score // 250 for score in score_distribution]

    rand = random.randint(0, 100000)
    rand = str(rand).zfill(6)
    current_time = str(int(time.time()))
    api_sig = rand + '/contest.standings?apiKey=' + api_key + '&contestId=' + \
        contest_id + '&groupCode=' + group_code + \
        '&time=' + current_time + '#' + api_secret
    hash = hashlib.sha512(api_sig.encode()).hexdigest()

    data = requests.get(f'https://codeforces.com/api/contest.standings?groupCode={group_code}&contestId={  contest_id}&apiKey={api_key}&time={current_time}&apiSig={rand+hash}').json()

    # DEBUG
    # pprint(data)

    final_standings = []
    data['result']['contest']['startTimeSeconds'] = datetime.datetime.fromtimestamp(
        data['result']['contest']['startTimeSeconds']).strftime('%Y-%m-%d %H:%M:%S')

    for index, participant in enumerate(data['result']['rows']):
        li = []

        handle_name = participant['party']['members'][0]['handle']
        li.append(handle_name)

        participant_score = 0

        for (i, problem) in enumerate(participant['problemResults']):
            # If no correct submission, continue
            if problem['points'] == 0:
                continue

            minutes_taken = problem['bestSubmissionTimeSeconds'] // 60

            penalty = problem['rejectedAttemptCount'] * 50
            # per-minute penalty stands for time taken for solve
            # penalty stands for number of incorrect submissions
            points = max(minPoints[i], score_distribution[i] -
                         minutes_taken * per_minute_penalty[i] - penalty)

            participant_score += points

        print(participant_score)
        li.append(participant_score)

        data['result']['rows'][index]['members'] = data['result']['rows'][index]['party']['members']
        del data['result']['rows'][index]['party']
        del data['result']['rows'][index]['successfulHackCount']
        del data['result']['rows'][index]['unsuccessfulHackCount']

        final_standings.append(li)

    # Sort the list in descending order of score

    participant_scores = [{'handle': participant[0], 'score': participant[1]}
                          for participant in final_standings]  # required json
    final_standings.sort(key=lambda x: x[1], reverse=True)
    with open(sys.argv[2], 'w') as file:
        json.dump(participant_scores, file)

    return final_standings


def main():
    group_code = 'NpnwJNnkjM'
    contest_id = sys.argv[1]

    # IMPORTANT: PROVIDE THIS MANUALLY
    arg_len = len(sys.argv)
    score_distribution = [int(sys.argv[i]) for i in range(3, arg_len)]

    # Generate your own API key and secret from https://codeforces.com/settings/api
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')

    final_standings = get_final_standings(score_distribution=score_distribution, api_key=api_key,
                                          api_secret=api_secret, contest_id=contest_id, group_code=group_code)

    print('Final Standings:')
    for i in range(len(final_standings)):
        print(f'{i+1}. {final_standings[i][0]} - {final_standings[i][1]}')


if __name__ == '__main__':
    main()
