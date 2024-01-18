### Getting Scores for Leaderboard

## Steps
- In a *.env*, add the **API_SECRET** and **API_KEY** from CF.
- Add contest-ids of required contests(make sure you are manager for those contests) in *final.json*.
- Also add the points for each problem in contest.
- Run *final.py* which generates **final.json**
- Have a list of present users in *data.xlsx*.
- Run **work.py** which removes absentees from the final json