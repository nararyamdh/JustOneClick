let textbox = document.querySelectorAll(".input-1");
let textbox_container = document.querySelectorAll(".textbox");
let icon = document.querySelectorAll(".icon");

textbox.addEventListener("focus", () => {
    icon.src = "/Volumes/AryaMD/Me/Project/JustOneClick/assets/icon/lock_f.svg"
    textbox_container.style.border = "2px solid rgb(17, 137, 243)";
});

textbox.addEventListener("blur", () => {
    icon.src = "/Volumes/AryaMD/Me/Project/JustOneClick/assets/icon/lock.svg"
    textbox_container.style.border = "1px solid #dddddd";
});

let preloader = document.querySelector(".preloader");
window.onload = function() {
  preloader.style.display = "None";
}