let mode=document.querySelector('#mode');

mode.addEventListener('click', (e)=>{
    let mode_img= document.querySelector('#mode-img');
    let b = document.body;
    let logout =document.querySelector('#logout')
    if(mode_img.className=="fas fa-sun"){
        mode.innerHTML='<i class="fas fa-moon" id="mode-img" ></i>';
        b.classList.toggle("dark-mode");
        mode.style.color = "white";
        logout.style.color = "white";
    }    
    else if (mode_img.className=="fas fa-moon"){
        mode.innerHTML='<i class="fas fa-sun" id="mode-img" ></i>';
        b.classList.toggle("dark-mode");
        mode.style.color = "black";

        logout.style.color = "black";

    }
})

