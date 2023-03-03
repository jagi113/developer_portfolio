let tags = [...document.getElementsByClassName('project-tag')]
tags.forEach(tag => {
    tag.addEventListener('click', function (e) {
        let tagID = e.target.dataset.tag
        let projectID = e.target.dataset.project

        fetch('http://127.0.0.1:8000/api/remove-tag', {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'project': projectID,
                'tag': tagID
            })
        }).then(response => response.json())
            .then(data => {
                e.target.remove()
            })
    })
})