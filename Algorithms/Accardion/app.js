let accStatus=true
let allItems=document.querySelectorAll('.acc-item')
function CloseAcc(el){
    
    for(let i=0;i<allItems.length;i++){
        allItems[i].querySelector('p').style.display='none'
        this.classList.toggle('active')
    }
    if(accStatus==true){
    el.nextElementSibling.style.display='none'
    accStatus=false
    }else{
    el.nextElementSibling.style.display='block'
    accStatus=true 
    }
}