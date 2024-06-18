const btns=document.querySelectorAll(".btns>li")
const forms=document.querySelectorAll(".forms>li>form")

btns.forEach((el,idx) => {
    el.addEventListener("click",()=>{
        forms[0].classList.remove("active")
        forms[1].classList.remove("active")

        if(idx==0){
            btns[0].style.borderBottom="2px solid rgb(3, 96, 3)"
            btns[1].style.borderBottom="2px solid rgb(197, 228, 204)"
            forms[1].classList.add("active")
        }else{
            btns[0].style.borderBottom="2px solid rgb(197, 228, 204)"
            btns[1].style.borderBottom="2px solid rgb(3, 96, 3)"
            forms[0].classList.add("active")
        }
        
    })
});