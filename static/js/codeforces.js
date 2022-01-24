function colorHandles(){

    const DOMhandles = document.getElementsByClassName('cf-handle');

    
    let handles = [];
    for(let i=0;i<DOMhandles.length;i++){
        handles.push(DOMhandles[i].innerHTML.trim());
    }
    
    const handleString = handles.join(';');
    
    if(handleString.trim() === ''){
        return;
    }

    const req = fetch(`https://codeforces.com/api/user.info?handles=${handleString}`);
    
    req.then((res)=>res.json()).then(
        (data)=>{
            console.log(data);
            if(data.status === "OK"){
                const resultList = data.result;
                resultList.forEach((user,index) => {
                    console.log(user.rank);
                    DOMhandles[index].classList.add(user.rank.replace(" ","-"));
                });
            }else{
                console.log('Some error occured');
            }
        }
    ).catch((err)=>console.log(err));
}

colorHandles();


