### Getting Scores for Leaderboard

## Steps
- Create a *.env* file.
- Add contest-ids of required contests(make sure you are manager for those contests) in *final.json*.
- Also add the points for each problem in contest.
- Run **final.py** which generates **final.json**
- Have a list of present users in *data.xlsx*.
- Run **fetch_handles.py** which modifies CF handles in *data.xlsx* to *updated_data.xlsx*
- Run **work.py** which removes absentees from the final json

## Note
- All the data is regenerated every time you run the scripts.