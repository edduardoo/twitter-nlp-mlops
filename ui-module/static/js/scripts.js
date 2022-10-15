const form = document.querySelector('#search_form');
form.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();
    let ipt = document.querySelector('#search_term')
    
    if(ipt.value.length < 5){
        ipt.classList.add("is-invalid");
        return
    } else {
        ipt.classList.remove("is-invalid");
        searchTweetsByTerm(ipt.value)
    }    

});

function searchTweetsByTerm(search_term){
    
    let results_div = document.querySelector('#results');
    let loading_div = document.querySelector('#loading');
    let error_div = document.querySelector('#error')
    results_div.innerHTML =  "";
    loading_div.style.display = "block";
    error_div.style.display = "none";
    
    let postObj = { 
        search_term: search_term
    }

    let post = JSON.stringify(postObj)
    let xhr = new XMLHttpRequest()
    xhr.open('POST', "/search", true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
    xhr.send(post);
    xhr.onload = function () {
        if(xhr.readyState == 4) {
            if(xhr.status === 200){
                let results_div = document.querySelector('#results')
                results_div.innerHTML =  xhr.responseText
                loading_div.style.display = "none";
            } else {                                
                loading_div.style.display = "none";
                error_div.style.display = "block";
            }
            
        }
    }
}


