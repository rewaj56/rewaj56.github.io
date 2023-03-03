const container = document.querySelector(".container");
const refreshBtn = document.querySelector(".refresh-btn");

const maxPaletteBoxes = 32;

const generatePalette = () => {
  // clearing the container
  container.innerHTML = "";
  for (let i = 0; i < maxPaletteBoxes; i++) {
    // generating a random hex color code
    let randomHex = Math.floor(Math.random() * 0xffffff).toString(16);
    randomHex = `#${randomHex.padStart(6, "0")}`;

    // creating a new 'li' element and inserting it into the container
    const color = document.createElement("li");
    color.classList.add("color");
    color.innerHTML = `<div class="rect-box" style="background: ${randomHex}"></div>
                            <span class="hex-value">${randomHex}</span>`;
    // adding click event to the current li element to copy the color
    color.addEventListener("click", () => copyColor(color, randomHex));
    container.appendChild(color);
  }
};

generatePalette(); //Calling function to generate palette on page load

const copyColor = (elem, hexVal) => {
  const colorElement = elem.querySelector(".hex-value");
  // Copying the hex value, updating the text to copied,
  // and changing the text back to original hex value after 1 second
  navigator.clipboard.writeText(hexVal).then(() => {
    colorElement.innerText = "Copied";
    setTimeout(() => colorElement.innerText = hexVal, 1000);
  }).catch(() => alert("Couldn't copy"));
}

refreshBtn.addEventListener("click", generatePalette);

// NOTE:
// document.querySelector() is a more versatile method
// that allows you to select elements using a wide range of CSS selectors,
// including class names, attributes, and pseudo-classes.
// It returns the first matching element it finds

// Math.random() generates a random number between 0 and 1.
// 0xffffff represents the maximum number in hexadecimal format, which is equivalent to the decimal number 16777215.
// Math.floor() rounds the random number down to the nearest integer.
// .toString(16) converts the integer into a hexadecimal string, with a base of 16.
// the code generates a random color code in the range #000000 to #ffffff

// The first argument of padStart() is the target length of the string,
// and the second argument is the padding character to use.
// The resulting string is then concatenated with a "#" symbol to create a valid hexadecimal color code.

// BackTick symbol in JavaScript is used to create a special type of text called a template
// This JavaScript code creates a new li element in the DOM and adds a color class to it.
