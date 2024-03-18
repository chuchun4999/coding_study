function dropdown(){
    const dropdown = document.getElementsByClassName("dropDown");
    const sub = document.getElementsByClassName('subMenu');
    dropdown[0].addEventListener('click',()=>{
    sub[0].style.cssText = 'display: block; max-height: 100px; animation-name: dropDown; animation-duration: .5s;';
    });
    dropdown[0].addEventListener('mouseleave',()=>{
    sub[0].style.display = 'none';
    });
}

dropdown();