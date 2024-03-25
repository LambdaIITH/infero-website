### Getting Scores for Leaderboard

## Steps
- Create a *.env* file.
- Run the *final.py* script using the format below.
   ```bash
        python final.py {contest_id_1} {num_question_1} {contest_id_2} {num_question_2} ...```
- Here, *contest_id* is the id of the contest and *num_question* is the number of questions in the contest.
- Then, have a *data.xlsx* file in the same directory which has presentees for all contests(don't keep separate ones for each contest).
- Run *fetch_handles.py* to get the handles of the presentees if they have changed.
    ```bash
        python fetch_handles.py```
- It generates a *updated_data.xlsx* with new handle names.
- Run work.py to finally keep only scores of people who have attempted the contest.
    ```bash
        python work.py {num_contests}```
- Here, *num_contests* is the number of contests you have data for.
- It generates a *final_data.json* file with the final scores.
- Take the *final_data.json* file and put it in the *data* folder.
- Finally, in the *data.html* file, add columns for more contests.


## Note
- All the data is regenerated every time you run the scripts.