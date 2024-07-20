const ticks = document.querySelectorAll('.tick');

function randomiseImage(){
    console.log(ticks);
    ticks.forEach( tick => {
        rand = Math.floor(Math.random()*10)+1;
        tick.src = "Ticks/"+rand+".png";
        console.log(rand+".png");

    });
}

function randomiseSize(){
    ticks.forEach( tick => {
        const scaleFactor = 0.9 + (Math.random() * 0.3);
        tick.style.transform = `translateX(${scaleFactor})`;
    });
}

function randomiseLocation(){
    ticks.forEach( tick => {
        const scaleFactory = -10 + Math.floor(Math.random() * 5);
        const scaleFactorx = Math.floor(Math.random() * 0.3);
        tick.style.transform = `translate(${scaleFactorx}, ${scaleFactory})`;
    });
}

function adjustLayoutForPrint() {
    const sections = document.querySelectorAll('.question-section');
    const pageHeight = 1122; // Pixel Height for A4 size

    let currentHeight = 0;

    sections.forEach(section => {
      const sectionHeight = section.offsetHeight;

      if (currentHeight + sectionHeight > pageHeight) {
        // Insert a page break if adding this section would exceed the page height
        const pageBreak = document.createElement('div');
        pageBreak.classList.add('page-break');
        section.before(pageBreak);
        currentHeight = 0;
      }

      currentHeight += sectionHeight;
    });
  }

function setDraggableFalse(){
    images = document.querySelectorAll('img');
    images.forEach(image => {
        image.draggable = false;
    });
}

window.onload = adjustLayoutForPrint;
randomiseImage();
randomiseSize();
randomiseLocation();
setDraggableFalse();