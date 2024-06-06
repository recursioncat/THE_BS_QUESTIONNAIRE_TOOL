document.addEventListener('DOMContentLoaded', function() {
    const questionContainers = document.querySelectorAll('.question-container');

    questionContainers.forEach(function(container) {
      const optionContainers = container.querySelectorAll('.option-container');

      optionContainers.forEach(function(optionContainer) {
        // Click listener on option container
        optionContainer.addEventListener('click', function() {
          const checkbox = optionContainer.querySelector('input[type="checkbox"]');
          checkbox.click();
        });
      });
    });

    // Click listener on all checkboxes (for single selection)
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('click', function() {
        checkboxes.forEach(function(otherCheckbox) {
          if (otherCheckbox !== checkbox) {
            otherCheckbox.checked = false;
          }
        });
      });
    });
  });