// //large-image-slider-start//

// function first() {
//     document.getElementById("slideimage").src = "../static/img/1.PNG";
// }

// function second() {
//     document.getElementById("slideimage").src = "../static/img/2.JPG";
// }

// function third() {
//     document.getElementById("slideimage").src = "../static/img/3.JPG";
// }

// function forth() {
//     document.getElementById("slideimage").src = "../static/img/4.JPG";
// }
// setTimeout(first, 2000);
// setInterval(second, 4000);
// setInterval(third, 6000);
// setInterval(forth, 8000);
// //large-image-slider-end//


//image-slider-StaticRange-start//
const productContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];


productContainers.forEach((item, i) => {
    let containerDimentions = item.getBoundingClientRect();
    let containerWidth = containerDimentions.width;


    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})

//image-slider-StaticRange-end//

//contact-form-start//

const inputs = document.querySelectorAll(".input");

function focusFunc() {
    let parent = this.parentNode;
    parent.classList.add("focus");
}

function blurFunc() {
    let parent = this.parentNode;
    if (this.value == "") {
        parent.classList.remove("focus");
    }
}

inputs.forEach((input) => {
    input.addEventListener("focus", focusFunc);
    input.addEventListener("blur", blurFunc);
});



//image-slider-StaticRange-start//




//login - part start//
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

//login - part end//

//new slider section start//
var myIndex = 0;
carousel();

function carousel() {

    var i;
    var x = document.getElementsByClassName("MYslider");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none"
    }
    myIndex++;
    if (myIndex > x.length) { myIndex = 1 }
    x[myIndex - 1].style.display = "block";
    setTimeout(carousel, 3000);
}

//new slider section end//