function toggleMenu() {
    // Basically makes it so that the objects with class = menu-links and hamburger-icon toggle open in their classname
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open")
    icon.classList.toggle("open")
}