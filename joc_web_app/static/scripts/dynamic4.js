let preloader = document.querySelector(".preloader");
window.onload = function() {
  preloader.style.display = "None";
}

let searchbox = document.getElementById("searchbox");
let search = document.getElementById("search");
let icon_search = document.getElementById("icon_search");

search.addEventListener("focus",() => {
    searchbox.style.outline = "2px solid rgb(16, 116, 204)";
    icon_search.src = "/Volumes/AryaMD/Me/Project/JustOneClick/assets/icon/search_f.svg";
});

search.addEventListener("blur",() => {
    searchbox.style.outline = "1px solid #ddd";
    icon_search.src = "/Volumes/AryaMD/Me/Project/JustOneClick/assets/icon/search.svg";
});