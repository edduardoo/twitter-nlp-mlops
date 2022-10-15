function searchTweetsByTerm(){
    
    let results_div = document.querySelector('#results');
    let loading_div = document.querySelector('#loading');
    results_div.innerHTML =  "";
    loading_div.style.display = "block";
    
    let postObj = { 
        search_term: document.querySelector('#search_term').value
    }

    let post = JSON.stringify(postObj)
    let xhr = new XMLHttpRequest()
    xhr.open('POST', "/search", true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
    xhr.send(post);
    xhr.onload = function () {
        if(xhr.readyState == 4 && xhr.status === 200) {
            let results_div = document.querySelector('#results')
            results_div.innerHTML =  xhr.responseText
            loading_div.style.display = "none";
        }
    }
}


