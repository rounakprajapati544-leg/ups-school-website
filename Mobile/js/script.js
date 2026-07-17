const menuBtn = document.getElementById("menuBtn");

const sidebar = document.getElementById("sidebar");

const overlay = document.getElementById("overlay");

menuBtn.onclick = function(){

sidebar.classList.add("active");

overlay.classList.add("active");

}

overlay.onclick = function(){

sidebar.classList.remove("active");

overlay.classList.remove("active");

}