
const visual_img = document.querySelector(".visual_img")
const arrows = document.querySelectorAll(".arrow")
const card_wrap = document.querySelector(".card_wrap")
const cards = [...document.querySelectorAll(".content_card")]
const slide = document.querySelector(".silde")
const empty_content = document.querySelector(".empty_content p")
const header = document.querySelector("header")
const headerHeight = header.offsetHeight

cards.forEach((element, index) => {
    element.addEventListener("mouseenter",(e)=>{
        console.log("mouseenter is active");
        empty_content.style.opacity = "0";
    })
    element.addEventListener("mouseleave",(e)=>{
        console.log("mouseleave is active");
        empty_content.style.opacity = "1";
    })
})

// empty_content.addEventListener("mouseenter",(e)=>{
//     console.log("mouseenter is active");
//     console.log(e);
// })
// empty_content.addEventListener("mouseleave",(e)=>{
//     console.log("mouseleave is active");
//     console.log(e);
// })


window.onscroll = function () {
    let windowTop = window.scrollY;
    // windowTop += 30
    // 스크롤 세로값이 헤더높이보다 크거나 같으면 
    // 헤더에 클래스 'drop'을 추가한다
    if (windowTop >= headerHeight+40) {
        header.classList.add("drop");
        header.classList.remove("nomal");
        visual_img.style.marginTop = "0"
    } 
    // 아니면 클래스 'drop'을 제거
    else {
        header.classList.add("nomal");
        header.classList.remove("drop");
        visual_img.style.marginTop = "-90px"
    }
};

// background-attachment: fixed;

var d1 = new Date(2014, 3, 1); // 2014-03-01
console.log(d1)
d1.setDate(0); // 2014-02-28 => 2월 마지막날
console.log(d1)