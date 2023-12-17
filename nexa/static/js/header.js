document.addEventListener('DOMContentLoaded', function() {
    let menu = document.querySelector('.menu-toggle');

    menu.addEventListener('click', function(){
        classes = document.querySelector('nav ul').classList.toggle("show");
        
        if (classes){
            menu.style.color = '#d7d3d3';
        }
        else {
            menu.style.color = '#f5f6f7'
        }
    });
})