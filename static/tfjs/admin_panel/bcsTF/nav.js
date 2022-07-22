const navLinks = document.querySelectorAll('.nav-link')
navLinks.forEach(link => {
  if (link.href == document.URL) {
    link.classList.add("active")
  } else {
    link.classList.remove("active")
  }
})

const dropdownContainers = document.querySelectorAll(".dropdown-container");

const dropdown = document.querySelectorAll(".dropdown-btn");
for (let i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function () {
    var dropdownContent = this.nextElementSibling;
    dropdownContainers.forEach(item => {
      item.classList.remove("show-dropdown-container")
      if (item.classList.contains("active-container") && item != dropdownContent) {
        item.classList.remove("active-container");
        item.previousElementSibling.classList.remove("clicked")
      }
    })
    if (dropdownContent.classList.contains("active-container")) {
      dropdownContent.classList.remove("show-dropdown-container");
      dropdownContent.classList.remove("active-container");
      dropdown[i].classList.remove("clicked");
    } else {
      dropdownContent.classList.add("show-dropdown-container");
      dropdownContent.classList.add("active-container");
      dropdown[i].classList.add("clicked");
    }
  });
}
const mainSection = document.querySelector("main")
mainSection.addEventListener("click", () => {
  dropdownContainers.forEach(item => {
    item.classList.remove("show-dropdown-container")
    item.classList.remove("active-container")
  })
  dropdown.forEach(item => {
    item.classList.remove("clicked");
  })
})

const deleteBtn = document.querySelectorAll(".trash, .dlt")

deleteBtn.forEach(btn => {
  btn.addEventListener("click", () => {
    btn.parentElement.parentElement.style.display = "none"
  })
})


const hamburger = document.querySelector(".hamburger")
const sideBarClose = document.querySelector(".sideBarClose")
const sideBarText = document.querySelectorAll(".nav-text")
const aside = document.querySelector(".aside-container")
const nav = document.querySelector("nav")
const main = document.querySelector("main")
const footer = document.querySelector("footer")

hamburger.addEventListener("click", () => {
  aside.classList.toggle("show-aside")
  aside.classList.contains("shrink-container") && aside.classList.remove("shrink-container")
})

sideBarClose.addEventListener("click", () => {
  aside.classList.remove("show-aside")
});

const updateSidebar = () => {
  if (expanded == 'true') {
    aside.classList.remove("shrink-container")
    nav.classList.remove("nav-expand")
    main.classList.remove("main-expand")
    footer.classList.remove("footer-expand")
    sideBarText.forEach(text => {
      text.classList.remove("d-none")
    });
    expandBtn.classList.remove('d-none')
    shrinkBtn.classList.add('invisible')
  }
  else {
    aside.classList.add("shrink-container")
    nav.classList.add("nav-expand")
    main.classList.add("main-expand")
    footer.classList.add("footer-expand")
    sideBarText.forEach(text => {
      text.classList.add("d-none")
    });
    expandBtn.classList.add('d-none')
    shrinkBtn.classList.remove('invisible')
  }
}

let expanded = localStorage.getItem("sidebar-expanded");
const shrinkBtn = document.querySelector(".shrink-btn");
let expandBtn = document.querySelector('.menu-expand-btn');

shrinkBtn.addEventListener("click", () => {
  expanded = expanded == 'true' ? 'false' : 'true';
  // Store value to local storage
  localStorage.setItem("sidebar-expanded", expanded);
  updateSidebar();
})
expandBtn.addEventListener("click", () => {
  expanded = expanded == 'true' ? 'false' : 'true';
  // Store value to local storage
  localStorage.setItem("sidebar-expanded", expanded);
  updateSidebar();
})


updateSidebar();