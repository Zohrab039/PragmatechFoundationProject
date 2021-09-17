let btn=document.createElement('button')
btn.innerHTML='Click Me'
let box=document.querySelector('.box')

box.appendChild(btn)
let baslangicGenislik=200
let baslangicHundurluk=300
btn.addEventListener('click',function(){
    let randR=Math.floor(Math.random()*255)
    let randG=Math.floor(Math.random()*255)
    let randB=Math.floor(Math.random()*255)
    baslangicGenislik+=30
    baslangicHundurluk+=30
    box.style.width=`${baslangicGenislik}px`
    box.style.height=`${baslangicHundurluk}px`
    box.style.background=`rgb(${randR},${randG},${randB})`
    console.log(randR,randG,randB)
})