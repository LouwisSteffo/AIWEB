var button1 = document.querySelector(".button-1");
var text1 = document.querySelector(".text-1");
var group1 = document.querySelector(".group-1");

var button2 = document.querySelector(".button-2");
var text2 = document.querySelector(".text-2");

var button3 = document.querySelector(".button-3");
var text3 = document.querySelector(".text-3");

button1.onclick = function () {
    setTimeout(text1.classList.add("active"), 2000);
};

button2.onclick = function () {
    setTimeout(text2.classList.add("active"), 2000);
}

button3.onclick = function () {
    setTimeout(text3.classList.add("active"), 2000);
}