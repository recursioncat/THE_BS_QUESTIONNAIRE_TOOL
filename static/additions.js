function addOption(qid){
    const questionContainer = document.getElementById(qid);
    const container = questionContainer.querySelector('#holder');
    const option = questionContainer.querySelector('#selection'); 
    const newOptionHTML = `
    <div class="option-container">
    <div>
      <input class="check" type="checkbox">
      <textarea class="option-text" type="text" placeholder="Write an Option Like The Allies"></textarea>
    </div>
    <div class="slider-container">
                    <input class="slider" type="range" min="0" max="100" value="0">
                    <input class="slider-value" value="0"> %
                </div>
  </div>
    `;
    container.insertAdjacentHTML('beforeend', newOptionHTML);

    if (option.value === 'Custom'){
        const cont = questionContainer.querySelectorAll('.slider-container');
        cont.forEach(opt => {
            opt.classList.add('show')
        });
    }

    checkbox(option, qid);
    setUpSlider();
    boxChecker();
}


function removeOption(questionId) {
    const container = document.getElementById(questionId);
    const area = container.querySelector('#holder');
    const optionContainers = area.querySelectorAll('.option-container');
    const lastOptionContainer = optionContainers[optionContainers.length - 1];
    if (lastOptionContainer) {
        area.removeChild(lastOptionContainer);
    }
}

let question_count = 2;


function addQuestion() {
    const main = document.querySelector('main');
    const questionId = `question-${question_count}`;

    // Create a new div element for the question container
    const newQuestion = document.createElement('div');
    newQuestion.setAttribute('draggable', 'true');
    newQuestion.classList.add('question-container');
    newQuestion.setAttribute('id', questionId);
    newQuestion.innerHTML = `
        <div class="top-region">
            <div>
                <i id="grip" class="fa-solid fa-grip-vertical"></i>
                <p class="question-number">Question ${question_count}</p>
            </div>
            <div class="properties">
                <select id="question-type" onchange="changeLayout(this, '${questionId}')">
                    <option>MCQ</option>
                    <option>Open-Ended</option>
                </select>
                <select onchange="giveSlider(this, '${questionId}'); checkbox(this, '${questionId}')" id="selection">
                    <option>Random</option>
                    <option>Perticular</option>
                    <option>Custom</option>
                </select>
                <button class="removeQuestion" onclick="removeQuestion('${questionId}')"><i class="fa-regular fa-circle-xmark"></i></button>
            </div>
        </div>
        <textarea class="question" type="text" placeholder="Write a Question Like Who won WW2?"></textarea>
        <div id="holder">
        <div class="option-container">
        <div>
          <input class="check" type="checkbox">
          <textarea class="option-text" type="text" placeholder="Write an Option Like The Allies"></textarea>
        </div>
        <div class="slider-container">
                    <input class="slider" type="range" min="0" max="100" value="0">
                    <input class="slider-value" value="0"> %
                </div>
      </div>
        </div>
        <button class="add-btn-option" onclick="addOption('${questionId}')">Add An Option</button>
        <button id="rem" class="add-btn-option" onclick="removeOption('${questionId}')">Remove An Option</button>
    `;

    // Append the new question container to the main element
    main.appendChild(newQuestion);

    // Increment question_count
    question_count++;
    disableDrag();
    attachEventListeners();
    setUpSlider();
    recalculateQuestionNumbers();
    boxChecker();
}


function changeLayout(option, question){
    const selected = option.value;
    const ques = document.getElementById(question);
    const area = ques.querySelector('#holder');
    const btn = ques.querySelectorAll('.add-btn-option');
    const other = option.closest('.properties').querySelector('#selection');

    switch(selected){
        case 'Open-Ended':
            for(i=0; i<btn.length; i++){
                btn[i].style.display = 'none';
            }
            area.innerHTML = `<textarea class="answer-region" readonly></textarea>`;
            other.style.display = 'none';
            break;
        case 'MCQ':
            for(i=0; i<btn.length; i++){
                btn[i].style.display = 'inline-block';
            }
            area.innerHTML = `<div class="option-container">
            <div>
                <input class="check" type="checkbox">
                <textarea class="option-text" type="text" placeholder="Write an Option Like The Allies"></textarea>
            </div>
            <div class="slider-container">
                <input class="slider" type="range" min="0" max="100" value="0">
                <input class="slider-value" value="0"> %
            </div>
        </div>
            `;
            other.style.display = 'inline-block';
            other.value = 'Random';
            break;
    }
}


function giveSlider(option, question){
    const selected = option.value;
    const ques = document.getElementById(question);
    const options = ques.querySelectorAll('.option-container');

    if (selected === 'Custom'){
        options.forEach(opt => {
            opt.querySelector('.slider-container').classList.add('show'); 
        });
    }

    else{
        options.forEach(opt => {
            opt.querySelector('.slider-container').classList.remove('show'); 
        });
    }

}

function checkbox(option, question){
    const selected = option.value;
    const ques = document.getElementById(question);
    const checkboxes = ques.querySelectorAll('.check');
    if (selected !== 'Perticular'){
        checkboxes.forEach(box =>{
            box.style.display = 'none';
        });
    }

    else{
        checkboxes.forEach(box =>{
            box.style.display = 'inline-block';
        });
    }
}


function removeQuestion(id){
    question = document.getElementById(id);
    question.remove();
    recalculateQuestionNumbers();
}


function recalculateQuestionNumbers() {
    const questionContainers = document.querySelectorAll('.question-container');
    questionContainers.forEach((container, index) => {
        const questionNumber = container.querySelector('.question-number');
        questionNumber.textContent = `Question ${index + 1}`;
    });
}


const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = '30px';
  this.style.height = (this.scrollHeight) + "px";
}

function boxChecker(){
    const boxes = document.querySelectorAll('.check');
    boxes.forEach(box => {
        box.addEventListener('input', (event) => {
            event.preventDefault();
            const target = event.target;
            console.log("Hello");
            const question = box.closest('.question-container');
            console.log(question)
            const checkboxes = question.querySelectorAll('.check');
            console.log(checkboxes);
            checkboxes.forEach(checkbox =>{
                console.log("yoyo");
                checkbox.checked = false;
            });
            if (!target.checked){
                target.checked = true;
            }
            else{
                target.checked = false;
            }
        });
    });
}

boxChecker();


