const draggables = document.querySelectorAll('.question-container');
const container = document.querySelector('main');
let isDragging = false;


function turnWhite(){
    all = document.querySelectorAll('.question-container');
    all.forEach(element => {
        element.style.backgroundColor = "white";
        element.style.filter = "blur(0px)";
    });
}

document.addEventListener('dragstart', (event) => {
    // Check if the dragged element is a question-container
    if (event.target.classList.contains('question-container')) {
        event.target.classList.add('dragging');
    }
});

document.addEventListener('dragend', (event) => {
    event.preventDefault();
    if (event.target.classList.contains('question-container')){
        event.target.classList.remove('dragging');
    }
    turnWhite();
})

document.addEventListener('dragover', (event) => {
    event.preventDefault();
    if (event.target.classList.contains('question-container')) {
        
        // Check if a drag operation is in progress to debounce the event
        if (!isDragging) {
            isDragging = true;
            setTimeout(() => {
                const afterElement = getDragAfterElement(event.clientY);
                const draggable = document.querySelector('.dragging');
                if (draggable) { // Check if draggable is not null
                    if (afterElement == null){
                        container.appendChild(draggable);
                    }
                    else{
                        
                        draggable.style.backgroundColor = "#FEB941";
                        draggable.style.filter = "blur(1px)";
                        container.insertBefore(draggable, afterElement);
                    }
                }
                isDragging = false;
            }, 50); // Adjust the debounce time as needed
        }
    } recalculateQuestionNumbers();
});

function getDragAfterElement(y){
    const draggableElements = [...document.querySelectorAll('.question-container:not(.dragging)')];

    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height/2;

        if (offset<0 && offset > closest.offset){
            return { offset: offset, element: child};
        }
        else{
            return closest;
        }

    }, {offset: Number.NEGATIVE_INFINITY }).element;

}

function disableDrag(){
    const draggeableObj = document.querySelectorAll('.question-container');
    draggeableObj.forEach( obj => {
        obj.draggable = false;
    });
}

function enableDrag(){
    const draggeableObj = document.querySelectorAll('.question-container');
    draggeableObj.forEach( obj => {
        obj.draggable = true;
    });
}

disableDrag();

function attachEventListeners() {
    const grips = document.querySelectorAll('#grip');
    grips.forEach(grip => {
        grip.addEventListener("mousedown", () => {
            enableDrag();
        });
        grip.addEventListener("dragstart", () => {
            enableDrag();
        });
    });

    document.addEventListener("mouseup", () => {
        disableDrag();
    });
    document.addEventListener("dragend", () => {
        disableDrag();
    });
}

attachEventListeners();
