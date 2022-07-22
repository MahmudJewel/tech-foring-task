const dot = document.querySelector(".slick-dots");
const titleArray = [
  "Business Cybersecurity",
  "Personal Cybersecurity",
  "Academy",
];
const classArray = ["ec-title", "pc-title", "pa-title"];
const dotList = dot.childNodes;
for (let i = 0; i < dotList.length; i++) {
  const span = document.createElement("span");
  span.innerText = titleArray[i];
  dotList[i].appendChild(span);
  dotList[i].classList.add(classArray[i]);
}
