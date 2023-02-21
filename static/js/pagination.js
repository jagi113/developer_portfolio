//GET SEARCH FORM for value and PAGE LINKS
let searchForm = document.getElementById('searchForm')
let pageLinks = [...document.getElementsByClassName('page')]

// ENSURE SEARCH FORM EXISTS
if (searchForm){
    pageLinks.forEach(item => {
    item.addEventListener('click', function(e){
        e.preventDefault()
        
        //GET THE PAGELINK ATTRIBUTE
        let page = this.dataset.page
        
        //ADD HIDDEN SEARCH INPUT TO FORM - so when we click we submit a new search with page value
        searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

        //SUBMIT FORM
        searchForm.submit()
        }
    )
    })
}
