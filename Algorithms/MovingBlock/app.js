/* let btn = document.createElement('button');
btn.innerHTML = 'click';
document.querySelector('.box').appendChild(btn);

btn.addEventListener('click', function() {
    document.querySelector('.box').style.backgroundColor='red';
}); */
/* let btn = document.createElement('button');
btn.innerHTML = 'click';
document.body.appendChild(btn);
let marginTopu = 0
btn.addEventListener('click', function() {
    document.querySelector('.box')
    marginTopu+=10
    box.style.top=`${marginTopu}px`
}); */
let box =document.querySelector('.box');
let up2=1
let left2=1
let right2=1
let down2=1
box.style.height=30 + 'px';
function up(){
    /* box.style.height=30 + 'px'; */
    box.style.bottom=30 * up2 + 'px';
    up2++;
}
box.style.height=30 + 'px';
function left(){
    box.style.left=30 + 'px';
    box.style.right=30 * left2 + 'px';
    left2++;
}
function right(){
    box.style.right=30 + 'px';
    box.style.left=30 * right2 + 'px';
    right2++;
}
function down(){
    box.style.bottom=30 + 'px';
    box.style.height=30 * down2 + 'px';
    down2++;
}