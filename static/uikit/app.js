// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  closeMessage();
});

function closeMessage(){
  let alertWrapper = document.getElementsByClassName('alert')
  let alertClose = document.getElementsByClassName('alert__close')

  if (alertWrapper) {
    [...alertClose].forEach(item => {
      item.addEventListener('click', ()=>{
        [...alertWrapper].forEach(i => {
          i.style.display = 'none'
          })
      })
    });
  }
}