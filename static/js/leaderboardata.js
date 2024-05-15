document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://dl.dropboxusercontent.com/scl/fi/y77upw0z1rjzdg6rh2xfw/leaderBoardData.json?rlkey=gt9qah7h4ci5ccsitj7jgfabb&st=dn1rnof0&dl=1';

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.users.length === 0) {
                console.error('No user data available');
                return;
            }

            const table = document.getElementById('leaderboardTable');
            const thead = table.createTHead();
            const tbody = table.createTBody();
            const row = thead.insertRow();

            // Assuming each user object has the same structure
            const headers = ['Rank', 'Handle', ...Object.keys(data.users[0]).filter(key => key.startsWith('contest')), 'Total'];
            headers.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header;
                row.appendChild(th);
            });

            data.users.forEach(user => {
                const tr = tbody.insertRow();
                headers.forEach(header => {
                    let field = header.toLowerCase();
                    if (field in user) {
                        const cell = tr.insertCell();
                        if (header === 'Handle') {
                            cell.innerHTML = `<a class='cf-handle' href='https://codeforces.com/profile/${user.handle}' target='_blank'>${user.handle}</a>`;
                        } else {
                            cell.textContent = user[field];
                        }
                    }
                });
            });

            // Call colorHandles here after the DOM has been updated
            colorHandles();
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
});

function colorHandles() {
  const DOMhandles = document.getElementsByClassName("cf-handle");

  let handles = [];
  for (let i = 0; i < DOMhandles.length; i++) {
    handles.push(DOMhandles[i].innerHTML.trim());
  }

  const handleString = handles.join(";");

  if (handleString.trim() === "") {
    return;
  }

  const req = fetch(
    `https://codeforces.com/api/user.info?handles=${handleString}`
  );

  req
    .then((res) => res.json())
    .then((data) => {
      if (data.status === "OK") {
        const resultList = data.result;
        resultList.forEach((user, index) => {
          if (!('rank' in user))
            user['rank'] = 'newbie';
          
          DOMhandles[index].classList.add(user.rank.replace(" ", "-"));
        });
      } else {
        console.log("Some error occurred");
      }
    })
    .catch((err) => console.log(err));
}
